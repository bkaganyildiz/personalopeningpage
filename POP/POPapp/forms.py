from django import forms
from .models import Background


class BackgroundImageForm(forms.Form):
    image = forms.ImageField()

class EditProfile(forms.Form) :
    image = forms.ImageField()
    name = forms.CharField()
    info = forms.CharField()

class AddInstanceForm(forms.Form) :
    picker = forms.CharField(widget=forms.Textarea,required=True)
    x = forms.IntegerField()
    y = forms.IntegerField()
class RemoveInstanceForm(forms.Form) :
    instance_id = forms.CharField(required=True)

class LoadDesignForm(forms.Form) :
    loadFile = forms.FileField()
