# streaming/views.py
from django.shortcuts import render
from django.http import StreamingHttpResponse
import os

VIDEO_FOLDER = 'streaming/videos'

def index(request):
    return render(request, 'index.html')

def video(request, filename):
    video_path = os.path.join(VIDEO_FOLDER, filename)
    response = StreamingHttpResponse(open(video_path, 'rb'), content_type='video/mp4')
    return response

def list_videos(request):
    videos = os.listdir(VIDEO_FOLDER)
    return render(request, 'videos.html', {'videos': videos})