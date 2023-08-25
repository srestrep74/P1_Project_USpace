from django.urls import path
from . import views


urlpatterns = [
    path('show_spaces' , views.viewSpaces , name='show_spaces'),
    path('add_space' , views.addSpace , name='add_space')
]