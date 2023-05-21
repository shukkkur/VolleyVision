from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
]
