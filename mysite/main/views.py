from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
	return HttpResponse("<h1> this is where html goes </h1>")
