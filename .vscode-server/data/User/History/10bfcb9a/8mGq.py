from django.urls import path
from . import views

urlpatterns = [
    path('', views.PdnoMain, name='pdnoMain'),
]