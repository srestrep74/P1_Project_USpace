from django.shortcuts import render
from Api.api_ubidots import spaces_status
from django.http import JsonResponse

def home(request):
    return render(request , 'Map/home.html' )

def spaces_data(request):
    spaces = spaces_status()
    return JsonResponse(spaces)