from django import forms

class CreateNewList(forms.Form):
	#the fields in the forum
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)

