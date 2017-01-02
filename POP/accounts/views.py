from django.contrib.auth import (
    authenticate ,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm , UserRegisterForm
from django.views.decorators.csrf import csrf_exempt
import POPapp
# Create your views here.

@csrf_exempt
def login_view(request) :
    form = UserLoginForm(request.POST or None)
    print(form)
    if form.is_valid() :
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        return redirect(POPapp.views.setBackground, username=username)

    return render(request , "accounts/templates/index.html",{})


@csrf_exempt
def register_view(request) :
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        return HttpResponse("User Registered")

    return render(request , "accounts/templates/index.html",{"form" : form})

def logout_view(request) :
    return render(request , "form.html",{})
