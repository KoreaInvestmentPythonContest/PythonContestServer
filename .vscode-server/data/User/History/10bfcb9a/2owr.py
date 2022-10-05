from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.PdnoMain.as_view(), name='PdnoMain'),
    path('<str:pk>', views.PdnoMain.as_view(), name='PdnoMain'),
]