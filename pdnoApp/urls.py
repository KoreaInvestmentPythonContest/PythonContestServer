from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.PdnoMain.as_view(), name='PdnoMain'),
    path('<str:symbol>/follow', views.MakeFollow.as_view(), name='MakeFollow'),
]