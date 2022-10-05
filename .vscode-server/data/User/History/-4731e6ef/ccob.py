from django.urls import path
from . import views

urlpatterns = [
    path('<str:pdno>', views.NewsFeed.as_view(), name='NewsFeed'),
]