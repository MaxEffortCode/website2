
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import ToDoList, Item


class DetailView(generic.DetailView):
	model = ToDoList
	template_name = 'mineapp/detail.html'
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return ToDoList.objects.all()
