from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_concerts, name='concerts-input'),
    path('concerts/', views.concerts, name='concerts-home'),
    path('saved/', views.saved_concerts, name='concerts-saved'),
]