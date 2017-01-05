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
from POPapp.models import PersonalInfo,Background ,ApplicationUser
import POPapp , pickle
from django.contrib.auth.models import User
from Application.Application import *
# Create your views here.

@csrf_exempt
def login_view(request) :
    form = UserLoginForm(request.POST or None)
    if form.is_valid() :
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        user = User.objects.get(username=username)
        request.session['username'] = username
        try :
            request.session['application'] = ApplicationUser.objects.get(user=user).app
        except ApplicationUser.DoesNotExist :
            ApplicationUser.objects.create(user=user, app=pickle.dumps(Application()))
            """try :
                ApplicationUser.objects.get(user=user).app = pickle.dumps(Application())
            except ApplicationUser.DoesNotExist :
                ApplicationUser.objects.create(user=user,app=pickle.dumps(Application()))"""
            request.session['application'] =  ApplicationUser.objects.get(user=user).app
        return redirect(POPapp.views.index, username=username)

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
        PersonalInfo.objects.create(user = user , name=user.username , image='default.png',info = '')
        Background.objects.create(user=user)
        request.session['username'] = user.username
        ApplicationUser.objects.create(user=user,app=pickle.dumps(Application()))
        return redirect(POPapp.views.index, username=user.username)

    return render(request , "accounts/templates/index.html",{"form" : form})

def logout_view(request) :
    print (request.session)
    try :
        username = request.session['username']
        user = User.objects.get(username=username)
        app = ApplicationUser.objects.get(user=user)
        app.app = request.session['application']
        app.save()
        del request.session['application']
        del request.session['username']
    except:
        pass
    return redirect('/')
