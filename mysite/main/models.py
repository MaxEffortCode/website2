from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
	#makes every todolist object linked with a specific user
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self): #default toString() method 
		return self.name

class Item(models.Model):	#django needs the tyoe of field "ToDoList" is, tell it that by using models.ForeignKey(object, ect)
							#models.cascade is defing how the object is delt with on deletion. cascade deletes entire object  
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

