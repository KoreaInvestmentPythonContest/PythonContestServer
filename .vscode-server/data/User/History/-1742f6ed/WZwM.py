"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from .views import View
from django.conf.urls import url, include
import debug_toolbar

urlpatterns = [
    path('', View.as_view() ),
    path('<str:pk>/recommand/', View.recPdno, name = 'recPdno'),
    path('admin/', admin.site.urls),
    path('pdno/', include('pdnoApp.urls')),
    path('search/', include(('feedApp.urls', 'feedApp'), namespace='feedApp')),
    path('myAuth/', include(('myAuth.urls','myAuth'),namespace='myAuth')),
    path('<int:pk>/comments/', View.comments_create, name='comments_create'),
    path('<str:user>/comments/<int:commentSeq>/delete/', View.comments_delete, name='comments_delete'),
    path('<int:newseq>/heart', View.add_heart, name='add_heart'),
]