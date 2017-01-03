from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Background, PersonalInfo, Connection
from .forms import BackgroundImageForm
from django.views.decorators.csrf import csrf_exempt
from .choices import *


@csrf_exempt
def editProfile(request, username):
    try:
        user = User.objects.get(username=username)
        pi = PersonalInfo.objects.get(user=user)
        pi.connections = Connection.objects.filter(user=user)
    except User.DoesNotExist:
        return redirect("/")

    context = {
        "person": pi,
        "user": user,
    }
    return render(request, "POPapp/templates/personalInfo.html", context)


def index(request, username):
    try:
        user = User.objects.get(username=username)
        background = Background.objects.get(user=user)
        pi = PersonalInfo.objects.get(user=user)
        pi.connections = Connection.objects.filter(user=user)
    except User.DoesNotExist:
        return redirect("/")
    except :
        Background.objects.create(user=user,name="Default", url="http://www.intrawallpaper.com/static/images/518164-backgrounds.jpg")
        background = Background.objects.get(user=user)

    context = {
        "background" : background.image,
        "person" : pi,
        "user" : user,
    }
    return render(request, "POPapp/templates/personalInfo.html", context)
# Create your views here.

@csrf_exempt
def setBackground(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)

        form = BackgroundImageForm(request.POST, request.FILES)
        if form.is_valid():
            background = Background.objects.get(user=user)
            background.image = form.cleaned_data['image']
            background.save()

            return redirect("/" + username)
        return redirect("/" + username + "/background")

    try:
        user = User.objects.get(username=username)
        background = Background.objects.get(user=user)
    except User.DoesNotExist:
        return redirect("")
    except :
        background = Background.objects.create(user=user, url="no-image.png", name="no_image")

    print("AAAAAAAAAAAAAAAAa", background.image)
    context = {
        "username" : username,
        "background" : background.image,
    }
    return render(request, "POPapp/templates/background.html", context)
