from django import forms
from .models import Background


class BackgroundImageForm(forms.Form):
    image = forms.ImageField()

class EditProfile(forms.Form) :
    image = forms.ImageField()
    name = forms.CharField()
    info = forms.CharField()
