from django.urls import path
from . import views

urlpatterns = [
   #path('', views.NewsFeed.as_view(), name='NewsFeed'),
    path('detail/', views.NewsFeed.as_view(), name='NewsFeed'),
    path('detailS/', views.SearchFeed.as_view(), name='SearchFeed'),
   # path('detail', views.SearchFeed.as_view(), name='detail'),
]