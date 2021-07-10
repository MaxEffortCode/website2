from django.urls import path

from . import views
'''
urlpatterns = [
    path("", views.index, name="index"),
]
'''

app_name = 'mineapp'
urlpatterns = [
    path('', views.DetailView.as_view(), name='detail'),
	 # ex: /mineapp/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
