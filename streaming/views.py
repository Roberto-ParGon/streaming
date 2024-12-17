# streaming/views.py
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
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

def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        fs = FileSystemStorage(location=VIDEO_FOLDER)
        fs.save(video_file.name, video_file)
        return redirect('list_videos')
    return render(request, 'upload.html')