from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('gen_pdf/', views.gen_pdf, name='gen_pdf'),
]