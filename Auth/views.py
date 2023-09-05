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

"""def signupAccount(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        email=form.cleaned_data['email']
                    )
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'signup.html', {'form': form, 'error': 'Username already taken. Choose a new username.'})
            
            else:
                return render(request, 'signup.html', {'form': form, 'error': 'Passwords do not match'})
        
        else:
            return render(request, 'signup.html', {'form': form})
    
    else:
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})"""


@login_required       
def logoutAccount(request):
    logout(request)
    return redirect('home')


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

def register(request):
    form = user_form()
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            _user = form.save()
            group = Group.objects.get(name='user')
            _user.groups.add(group)
            user_m.objects.create(user=_user, username=_user.username)
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
    return render(request, 'signup.html')