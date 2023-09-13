from django.shortcuts import render
from .forms import user_form
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


from django.db.models import Q

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

    # Ejecuta la consulta combinada
    spaces = Space.objects.filter(query)

    return render(request, 'searching.html', {'searchTerm': searchTerm, 'spaces': spaces})


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
            messages.info(request, 'Usuario o contrasena son incorrectos')
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
            user_m.objects.create(user=_user, username=_user.username)
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
        
    return render(request, 'signup.html', {'form': form})