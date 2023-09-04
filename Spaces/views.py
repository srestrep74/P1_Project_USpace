from django.shortcuts import render , redirect
from Api.api_ubidots import spaces_status
from django.http import JsonResponse
from Admins.models import Space
from django.core import serializers
import json


def home(request):
    return render(request , 'Map/home.html' )

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
    return render(request, "Map/space.html" , {'space':space})