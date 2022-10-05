from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsFeed.as_view(template_name='newsFeed.html'), name='NewsFeed'),
   # path('detail', views.SearchFeed.as_view(), name='detail'),
]