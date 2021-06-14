from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	#item = ls.item_set.get(id=1)
	#return render(response, "main/base.html", {"name":ls.name})
	return render(response, "main/list.html", {"ls":ls})


def v1(response):
	return HttpResponse("<h1> v1 </h1>")


def home(response):
	return render(response, "main/home.html", {})

def create(response): #response takes in the html request types "get", "post", ect. defaults to "GET"
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			#grabs data from field "name"
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
	else:
		form = CreateNewList()
	return render(response, "main/create.html", {"form":form})

