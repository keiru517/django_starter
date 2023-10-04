from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name="index"),  
    path('upload', views.upload, name="upload"),  
    path('chat', views.chat, name='chat'),
    path('format', views.format, name='format'),
    path('channel_chat', views.channel_chat, name='channel_chat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)