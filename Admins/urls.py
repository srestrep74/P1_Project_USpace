from django.urls import path
from . import views


urlpatterns = [
    path('show_spaces' , views.viewSpaces , name='spaces')
]