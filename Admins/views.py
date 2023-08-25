from django.shortcuts import render
from .models import *


def viewSpaces(request):
    searchTerm = request.GET.get('searchSpace')
    if searchTerm:
        spaces = Space.objects.filter(name__icontains=searchTerm)
    else:
        spaces = Space.objects.all()

    return render(request, 'spaces.html', {'searchTerm': searchTerm, 'spaces': spaces})