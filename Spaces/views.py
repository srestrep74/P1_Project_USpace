from django.shortcuts import render , redirect
from Api.api_ubidots import spaces_status
from django.http import JsonResponse
from Admins.models import Space
from django.core import serializers
import json
from .models import Review
from .forms import comment_form
from Auth.decorators import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request , 'Map/home_user.html' )

def spaces_data(request):
    spaces = Space.objects.all()
    json_spaces = {}
    for space in spaces:
        json_spaces[space.id] = {
            'id' : space.id,
            'name' : space.name,
            'description' : space.description,
            'availability' : space.availability,
            'classification' : space.classification,
            'latitude' : space.latitude,
            'longitude' : space.longitude

        }
    json_spaces = json.dumps(json_spaces)
    return JsonResponse(json_spaces, safe=False)


def space_info(request, pk):
    space = Space.objects.get(id=pk)
    form = comment_form()
    if request.method == 'POST':
        rating = 0
        space_id = pk
        user_id = request.user.id
        comment = request.POST.get('comment')
        print(comment)

    return render(request, "Map/space.html" , {'space':space, 'form' : form})