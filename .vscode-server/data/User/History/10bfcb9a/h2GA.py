from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdnoMain, name='pdnoMain'),
]