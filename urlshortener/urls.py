from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short/', views.short_link, name='short_link'),
    path('l/<link_hash>/', views.use_link, name='use_link'),
]