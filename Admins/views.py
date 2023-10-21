from django.shortcuts import render, redirect
from .models import *
from Spaces.models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import *


def showReports(request):
    damages = Damage.objects.filter()

    return render(request, 'view_reports.html', {'damages': damages})


def fixedDamage(request, id):
    damage = Damage.objects.get(id=id)
    damage.solved = True
    damage.save()
    return redirect('view_reports')


def viewSpaces(request):
    searchTerm = request.GET.get('searchSpace')
    if searchTerm:
        spaces = Space.objects.filter(name__icontains=searchTerm)
    else:
        spaces = Space.objects.all()

    return render(request, 'spaces.html', {'searchTerm': searchTerm, 'spaces': spaces})


def addSpace(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)  # Añade request.FILES
        if form.is_valid():
            space = form.save(commit=False)
            if 'image' in request.FILES:
                space.image = request.FILES['image']
            space.save()
            return redirect('show_spaces')
    
    else:
        form = SpaceForm()
    
    return render(request, 'add_space.html', {'form': form})


def editSpace(request, id):
    space_form, error = None, None
    try:
        space = Space.objects.get(id=id)
        if request.method == 'POST':
            space_form = SpaceForm(request.POST, request.FILES, instance=space)
            if space_form.is_valid():
                space_form.save()
                return redirect('show_spaces')
        else:
            space_form = SpaceForm(instance=space)

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un espacio con el ID {id}.'

    return render(request, 'edit_space.html', {'space_form': space_form, 'error': error})


def deleteSpace(request, id):
    space = Space.objects.get(id=id)
    space.delete()
    return redirect('show_spaces')