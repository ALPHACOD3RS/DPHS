from django import views
from django.urls import URLPattern, path, include
from . import views

URLPattern = [
    path('login/', views.login)
]