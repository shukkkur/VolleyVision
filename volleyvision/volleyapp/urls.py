from django.urls import path
from . import views


app_name = 'volleyapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
    path('clean_cache/', views.clean_cache, name='clean_cache'),
    path('<path:path>/', views.download, name='download'),
]
