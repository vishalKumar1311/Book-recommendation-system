from django.contrib import admin
from django.urls import path   
from .import views

urlpatterns = [
    path('', views.home),
    path('recommend/',views.recommend ,name="recommend"),
    path('recommend_books/',views.recommend_books ,name="recommend_books"),
   
]
