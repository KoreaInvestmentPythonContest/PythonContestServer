from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsFeed.as_view(), name='NewsFeed'),
    path('<str:name>', views.NewsFeed.as_view(), name='SearchFeed'),
]