from django.shortcuts import render, redirect
from .forms import RegisterForm



# Create your views here.
# TODO Create a deletion option
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/home")
	else:
		form = RegisterForm()

	form = RegisterForm()
	return render(response, "register/register.html", {"form":form})
