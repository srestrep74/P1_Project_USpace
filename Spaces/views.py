from django.shortcuts import render , redirect
from django.http import JsonResponse
from Admins.models import Space
from django.core import serializers
import json
from .models import Comment
from .forms import comment_form
from Auth.decorators import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from Auth.models import *


def home(request):
    return render(request , 'Map/home_user.html')


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
    comments = Comment.objects.all()
    if request.method == 'POST':
        rating = 0
        user = request.user
        comment = request.POST.get('comment')
        rev = Comment(
            rating = rating,
            space = space,
            comment = comment,
            user = user
        ) 
        rev.save()
        print(comment)
        return redirect("/")

    return render(request, "Map/space.html" , {'space':space, 'comments':comments})