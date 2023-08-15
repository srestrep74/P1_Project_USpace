from django.shortcuts import render
from Api.api_ubidots import spaces_status


def home(request):
    spaces = spaces_status()
    return render(request , 'Map/home.html' , {'spaces' : spaces} )