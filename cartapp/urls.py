
from django.contrib import admin
from django.urls import path
from cartapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
]
