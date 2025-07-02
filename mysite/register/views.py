from django.shortcuts import render, redirect
# import the new form from the forms.py
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})
