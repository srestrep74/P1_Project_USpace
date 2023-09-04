from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupAccount, name='signup'),
    path('logout/', views.logoutAccount, name='logout'),
    path('login/', views.loginAccount, name='login'),
    path('search_spaces/' , views.searchSpaces , name='search_spaces'),
]