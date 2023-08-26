from django.shortcuts import render
from .forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User

def signupAccount(request):
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
        return render(request, 'signup.html', {'form': form})


@login_required       
def logoutAccount(request):
    logout(request)
    return redirect('home')


def loginAccount(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request,'login.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
    else:
        login(request,user)

    return redirect('home')