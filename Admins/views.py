from django.shortcuts import render, redirect
from .models import *
from .forms import *


def viewSpaces(request):
    searchTerm = request.GET.get('searchSpace')
    if searchTerm:
        spaces = Space.objects.filter(name__icontains=searchTerm)
    else:
        spaces = Space.objects.all()

    return render(request, 'spaces.html', {'searchTerm': searchTerm, 'spaces': spaces})


def addSpace(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_space')
    
    else:
        form = SpaceForm()
    
    return render(request, 'add_space.html', {'form': form})