from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	#item = ls.item_set.get(id=1)
	#return render(response, "main/base.html", {"name":ls.name})
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.complete = True
				else:
					item.complete = False


				item.save()


		elif response.POST.get("newItem"):
			txt = response.POST.get("new")

			if len(text) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")


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
			#prevents sql injection attacks
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateNewList()
	return render(response, "main/create.html", {"form":form})

