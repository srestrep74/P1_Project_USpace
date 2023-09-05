from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('logout/', views.logoutAccount, name='logout'),
    path('login/', views.login, name='login'),
]