from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('logout/', views.logoutAccount, name='logout'),
    path('login/', views.login, name='login'),
    path('search_spaces/' , views.searchSpaces , name='search_spaces'),
    path('update_user/<int:pk>' , views.updateUser, name='update_user'),
    path('create_reminder/<int:user>/<int:space>' , views.createReminder, name='create_reminder'),
    path('comment/<int:space>', views.comment, name='comment'),
    path('report_damage/', views.reportDamage, name='report_damage')
]