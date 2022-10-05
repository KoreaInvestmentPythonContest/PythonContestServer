from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsFeed.as_view(), name='NewsFeed'),
    path('signup/', views.signup, name='SearchFeed'),
   # path('detail', views.SearchFeed.as_view(), name='detail'),
]