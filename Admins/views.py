from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
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


def editSpace(request, id):
    space_form, error = None, None
    try:
        space = Space.objects.get(id=id)
        if request.method == 'GET':
            space_form = SpaceForm(instance=space)
        else:
            space_form = SpaceForm(request.POST, instance=space)
            if space_form.is_valid():
                space_form.save()
                return redirect('show_spaces')

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un espacio con el ID {id}.'

    return render(request, 'edit_space.html', {'space_form': space_form, 'error': error})
