from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),#""<- directory in url, views.index is the file served, name="index" is function ran from views.py
]
