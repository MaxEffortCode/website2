from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.views.generic import TemplateView



# Django provides base view classes which will suit a wide range of applications. All views inherit from the View 
# class, which handles linking the view into the URLs, HTTP method dispatching and other common features. 
# RedirectView provides a HTTP redirect, and TemplateView extends the base class to make it also render a template.

app_name = 'main'
urlpatterns = [




path("<int:id>", views.index, name="index"),

path("vote/", views.view, name="vote"),

path("vote/<int:list_id>", views.vote, name="vote"),




path("", views.home, name ="home"),
path("home/", views.home, name ="home"),
path("create/", views.create, name="create"),

#""directory in url, views.v1 is the function v1() ran from views.py dont know what name is for
path("v1/", views.v1, name="view 1"),
path("view/", views.view, name="view"),
path('<int:item_id>/vote/', views.vote, name='vote'),
path('<int:item_id>/results/', views.ResultsView.as_view(), name='results'),



]
