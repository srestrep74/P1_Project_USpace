from django.urls import path
from . import views


urlpatterns = [
    path('show_spaces' , views.viewSpaces , name='show_spaces'),
    path('add_space' , views.addSpace , name='add_space'),
    path('edit_space/<int:id>' , views.editSpace , name='edit_space'),
    path('delete_space/<int:id>' , views.deleteSpace , name='delete_space'),
    path('view_report/' , views.deleteSpace , name='view_report'),
]