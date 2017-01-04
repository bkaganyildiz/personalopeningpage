from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from .models import Background, PersonalInfo, Connection
from .forms import BackgroundImageForm , AddInstanceForm, RemoveInstanceForm, LoadDesignForm
from django.views.decorators.csrf import csrf_exempt
from .choices import *
from Application.Application import *
import pickle
import os


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


@csrf_exempt
def index(request, username):
    if request.session.has_key('username') :
        #del request.session['application']
        if request.session.has_key('application'):
            app = pickle.loads(request.session['application'])
        else:
            app = Application()
            request.session['application'] = pickle.dumps(app)

        username = request.session['username']
        user = User.objects.get(username=username)
        try :
            background = Background.objects.get(user=user)
        except :
            pass
        pi = PersonalInfo.objects.get(user=user)
        pi.connections = Connection.objects.filter(user=user)
        print("HEY", app.available())
        context = {
            "person" : pi,
            "user" : user,
        }

        if request.POST.has_key('load'):
            print request.POST
            app.load(request.POST['componentName'])
            print app
            request.session['application'] = pickle.dumps(app)
        elif request.POST.has_key('add_instance'):
            form = AddInstanceForm(request.POST or None)
            print form
            if form.is_valid():
                method = form.cleaned_data['picker']
                x = form.cleaned_data['x']
                y = form.cleaned_data['y']
                app.addInstance(method,x,y)
                request.session['application'] = pickle.dumps(app)

        elif request.POST.has_key('remove_instance'):
            form = RemoveInstanceForm(request.POST or None)
            print form
            if form.is_valid():
                method = form.cleaned_data['instance_id']
                app.removeInstance(method)
                request.session['application'] = pickle.dumps(app)
        elif request.POST.has_key('load_des'):
            form = LoadDesignForm(request.POST , request.FILES)
            if form.is_valid() :
                loadFile = form.cleaned_data['loadFile']
                app.loadDesign(loadFile)
                request.session['application'] = pickle.dumps(app)
        elif request.POST.has_key('save_des'):
            #save_path = settings.BASE_DIR
            app.saveDesign( "design.txt")
            context['des_url'] = settings.BASE_DIR + "/design.txt"
        context['available'] = app.available()
        if not app.loaded() :
            context['loaded'] = ' '
        else :
            context['loaded'] = app.loaded()

        context['instances'] = app.instances()
        return render(request, "POPapp/templates/index.html", context)
    else :
        print (request.session.has_key('username'))
        return redirect ("/")
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
