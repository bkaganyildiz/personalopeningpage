from django import forms
from django.contrib.auth import (
    authenticate ,
    get_user_model,
    login,
    logout
)

User = get_user_model()

class UserLoginForm(forms.Form) :
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self , *args , **kwargs) :
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password = password)
        if username and password :
            user = authenticate(username=username, password = password )
            if not user :
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password) :
                raise forms.ValidationError("Incorrect password")
            if not user.is_active :
                raise forms.ValidationError("This user is not active")
            return super(UserLoginForm , self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = [
            'first_name' ,
            'last_name' ,
            'username' ,
            'email' ,
            'password'
        ]
    def cleaned_data(self) :
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
