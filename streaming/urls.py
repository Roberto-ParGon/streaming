# streaming/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<str:filename>/', views.video, name='video'),
    path('videos/', views.list_videos, name='list_videos'),
]