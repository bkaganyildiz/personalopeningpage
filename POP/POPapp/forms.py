from django import forms
from .models import Background


class BackgroundImageForm(forms.Form):
    image = forms.ImageField()

class EditProfile(forms.Form) :
    image = forms.ImageField(required=True)
    name = forms.CharField(required=True)
    info = forms.CharField(required=True)

class AddInstanceForm(forms.Form) :
    picker = forms.CharField(widget=forms.Textarea,required=True)
    x = forms.IntegerField()
    y = forms.IntegerField()
class RemoveInstanceForm(forms.Form) :
    instance_id = forms.CharField(required=True)

class LoadDesignForm(forms.Form) :
    loadFile = forms.FileField()

class CallMethodForm(forms.Form) :
    mid = forms.CharField(required=True)
    method = forms.CharField(widget=forms.Textarea,required=True)
    param0 = forms.CharField(required=False)
    param1 = forms.CharField(required=False)
    param2 = forms.CharField(required=False)
