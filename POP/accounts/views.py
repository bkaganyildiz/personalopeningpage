from django.contrib.auth import (
    authenticate ,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserLoginForm , UserRegisterForm
# Create your views here.

def login_view(request) :
    title = "Login"
    print "title"
    print request.POST
    #form = UserLoginForm(request.POST or None)
    #if form.is_valid() :
        #username = form.cleaned_data.get("username")
        #password = form.cleaned_data.get('password')
        #   print ("hello")
        #return HttpResponse("Here's the text of the Web page.")
    return render(request , "index.html",{})


def register_view(request) :
    form = UserRegisterForm(request.POST or None)

    return render(request , "index.html",{"form" : form})

def logout_view(request) :
    return render(request , "form.html",{})
