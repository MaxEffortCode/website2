
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import ToDoList, Item


def index(request):
    latest_question_list = ToDoList.objects.order_by('-name')[:5]
    output = ', '.join([q.name for q in latest_question_list])
    return HttpResponse(output)


class IndexView(generic.ListView):
	template_name = 'mineapp/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		time = timezone.now()
		#pub_date__lte is less than or equal to '-' in -pub_date is to order from new -> old
		return ToDoList.objects.filter(name__lte=timezone.now()).order_by('-name')[:10]


class DetailView(generic.DetailView):
	model = ToDoList
	template_name = 'mineapp/detail.html'
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return ToDoList.objects.all()

class ResultsView(generic.DetailView):
	model = ToDoList
	template_name = 'mineapp/results.html'
