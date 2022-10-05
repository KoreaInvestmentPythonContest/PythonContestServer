from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsFeed.as_view(), name='NewsFeed'),
]