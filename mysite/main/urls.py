from django.urls import path

from . import views

urlpatterns = [
#we are passing the int:id to views.py



path("<int:id>", views.index, name="index"),

path("", views.index, name ="index"),
path("home/", views.home, name ="home"),
path("create/", views.create, name="create"),

#""directory in url, views.v1 is the function v1() ran from views.py dont know what name is for
path("v1/", views.v1, name="view 1"),

]
