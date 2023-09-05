from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('spaces_data/',views.spaces_data, name='spaces_data'),
    path('space_info/<int:pk>',views.space_info, name='space_info')
]