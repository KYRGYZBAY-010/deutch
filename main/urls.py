from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hoem, name='home'),
    path('gramatic/', views.gramatic, name='gramatic'),
    path('toppic/', views.toppic, name='toppic'),
    path('video-lesson/', views.lesson, name='video_lesson'),
    path('test/', views.test, name='test'),
    path('register/', views.register, name='register'),
    path('login_user', views.login_user, name='login'),

]