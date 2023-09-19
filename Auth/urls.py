from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('logout/', views.logoutAccount, name='logout'),
    path('login/', views.login, name='login'),
    path('search_spaces/' , views.searchSpaces , name='search_spaces'),
    path('create_reminder/<int:user>/<int:space>' , views.createReminder , name='create_reminder'),
]