from django import forms

# to do list form
class CreateNewList(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    check = forms.BooleanField(required=False)