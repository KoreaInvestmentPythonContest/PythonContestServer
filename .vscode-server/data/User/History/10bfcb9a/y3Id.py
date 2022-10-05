from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>', views.PdnoMain.as_view(), name='PdnoMain'),
]