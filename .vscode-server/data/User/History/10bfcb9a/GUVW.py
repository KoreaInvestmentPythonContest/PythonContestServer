from django.urls import path
from . import views

urlpatterns = [
    path('', views.PdnoMain.as_view(), name='PdnoMain'),
]