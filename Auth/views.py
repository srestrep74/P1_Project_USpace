from django.shortcuts import render
from .forms import user_form, user_update_form
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.models import Group 
from Admins.models import Space
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .decorators import *
from Spaces.models import *
from Spaces.forms import *
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail, EmailMessage
from USpace.settings import EMAIL_HOST_USER
from django.utils import timezone


def send_notifications():
    current_time = timezone.now().astimezone(timezone.get_current_timezone())

    notifications = Notification.objects.filter(
        remember_to__lt=current_time,
        sent=False
    )

    for notification in notifications:
        print(notification.space_id)
        space = Space.objects.get(id=notification.space_id)
        usr = User.objects.get(id=notification.user_id)
        send_mail(
            f'{space.name}',
            f'¡Hola, {usr.username}! \n Te notificamos que {space.name.lower()} en estos momentos se encuentra {space.get_availability_display().lower()}',
            EMAIL_HOST_USER,
            [f'{usr.email}']
        )

    notifications.update(sent=True)


scheduler = BackgroundScheduler()
scheduler.add_job(send_notifications, 'cron', minute='*')
scheduler.start()


@login_required
def createReminder(request, user, space):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            usr = User.objects.get(pk = user)
            space_obj = Space.objects.get(pk = space)
            notification.user_id = usr.id
            notification.space_id = space_obj.id
            notification.save()
            messages.success(request, 'El recordatorio se ha agendado correctamente')
            return redirect('search_spaces')
        
    else:
        form = NotificationForm()
        space_obj = Space.objects.get(pk = space)

    return render(request, 'create_reminder.html', {'form': form, 'space': space_obj})


def searchSpaces(request):
    searchTerm = request.GET.get('searchSpace')
    selected_filters_list = request.GET.getlist('filter')
    # Convierte la lista en una cadena separada por comas
    selected_filters = ','.join(selected_filters_list)
    # Guarda los filtros seleccionados en una cookie
    response = HttpResponse(render(request, 'searching.html', {'searchTerm': searchTerm}))
    response.set_cookie('selectedFilters', selected_filters)
    # Inicializa una consulta vacía
    query = Q()

    if searchTerm:
        # Agrega la condición de búsqueda a la consulta
        query &= Q(name__icontains=searchTerm)

    if selected_filters_list:
        # Agrega las condiciones de filtro a la consulta
        filter_q = Q()
        for filter_value in selected_filters_list:
            if filter_value == 'Disponible':
                filter_q &= Q(availability=0)
            elif filter_value == 'Ocupado':
                filter_q &= Q(availability=1)
            elif filter_value == 'Escenario deportivo':
                filter_q &= Q(classification=0)
            elif filter_value == 'Zona de descanso':
                filter_q &= Q(classification=2)
            elif filter_value == 'Mesa de restaurante':
                filter_q &= Q(classification=1)

        query &= filter_q

    spaces = Space.objects.filter(query)
    success_message = None
    if messages.get_messages(request):
        success_message = messages.get_messages(request).__str__()

    return render(request, 'searching.html', {'searchTerm': searchTerm, 'spaces': spaces, 'success_message': success_message})


@login_required       
def logoutAccount(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuario o contraseña son incorrectos')
            return redirect('login')
    return render(request, 'login.html')


@unauthenticated_user
def register(request):
    form = user_form()
    if request.method == 'POST':
        form = user_form(request.POST)
        print(form)
        if form.is_valid():
            _user = form.save()
            group = Group.objects.get(name='user')
            _user.groups.add(group)
            user_m.objects.create(user=_user, username=_user.username, email=_user.email)
            messages.success(request, '¡Hola, ' + form.cleaned_data.get('username') + '! Tu cuenta ha sido creada exitosamente, ahora puedes inciar sesión.')
            return redirect('login')
        
    return render(request, 'signup.html', {'form': form})

def update_user(request, pk):
    _user = user_m.objects.get(id=pk)
    __user = _user.user
    form = user_update_form(instance = _user)
    if request.method == 'POST':
        form = user_update_form(request.POST,request.FILES,  instance=_user)
        if form.is_valid():
            form.save()
            __user.username = _user.username
            __user.email = _user.email
            __user.save()
            return redirect('/')
    context = {'form' :form}
    return render(request, 'update_user.html' , context)
