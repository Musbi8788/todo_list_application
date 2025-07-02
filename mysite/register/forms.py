from django import forms
# import the django built in forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """A class for the manage the registeration

    Args:
        UserCreationForm (_type_): _description_
    """
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        """add new form into django built in form and show how the form will be arrange
        """
        model = User
        fields = [
            "username", "phone", "email", "password1", "password2"
            ]
