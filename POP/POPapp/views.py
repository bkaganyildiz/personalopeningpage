from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from .models import Background, PersonalInfo, Connection ,ApplicationUser
from .forms import BackgroundImageForm , AddInstanceForm, RemoveInstanceForm, LoadDesignForm , CallMethodForm
from django.views.decorators.csrf import csrf_exempt
from .choices import *
from Application.Application import *
import pickle
import os

@csrf_exempt
def deleteSession(request, username):
    del request.session['application']
    user = User.objects.get(username=username)
    ApplicationUser.objects.get(user=user).delete()
    return redirect(index, username=username)


@csrf_exempt
def load_component(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))
        
    
        app.load(body['componentName'])
        
     
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'loaded_components' : app.loaded(),
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def add_instance(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))
        

        app.addInstance(
            body['componentName'], 
            int(body['x']), 
            int(body['y'])
        )
        
       
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'loaded_instances' : app.instances(),
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def remove_instance(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))
        

        app.removeInstance(body['id'])
        
       
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'loaded_instances' : app.instances(),
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def call_method(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))
        

        app.callMethod(
            body['key'],
            body['method'],
            *body['args'].split(',')
        )
        
       
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'loaded_instances' : app.instances(),
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def execute(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        app.execute()
        return render(request, "POPapp/templates/index2.html", {})

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
def postblog(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))

        print "\n\n\n\n\n\n", body['key'], body['content']

        content = app.callMethod(
            body['key'],
            'setContent',
            body['content']
        )

        
        print "\n\n\n\n\n", content 
       
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'content' : content,
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def fetch_comic(request, username):
    if request.session.has_key('username') :
        username = request.session['username']
        user = User.objects.get(username=username)

        appUser = ApplicationUser.objects.get(user=user)
        if not request.session.has_key('application'):
            request.session['application'] = appUser.app

        app = pickle.loads(request.session['application'])
        body = json.loads(request.body.decode('utf-8'))

        resp = app.callMethod(
            body['key'],
            'fetch_comic',
            body['num']
        )
       
        appUser.app = pickle.dumps(app)
        appUser.save()
        request.session['application'] = appUser.app

        return JsonResponse({
            'status': True,
            'comic' : resp,
        })
    else:
        return JsonResponse({
            'status': False,
        })


@csrf_exempt
def index(request, username):
   
    if request.session.has_key('username'):
        username = request.session['username']
        user = User.objects.get(username=username)

        try:
            appUser = ApplicationUser.objects.get(user=user)
            app = pickle.loads(appUser.app)
            if not request.session.has_key('application'):
                request.session['application'] = appUser.app

        except ApplicationUser.DoesNotExist:
            app = Application()
            appUser = ApplicationUser.objects.create(user=user, app=pickle.dumps(app))
            request.session['application'] = appUser.app

        context = {
            "user" : user,
            'available' : app.available(),
            'loaded' : app.loaded(),
            'instances' : app.instances(),
        }

        if request.method == 'POST' :
            print "hello asdasda"
            app.execute()
            return render(request, "POPapp/templates/index2.html", context)

        print "asdasdakwemkajskdjksadjs"   
        return render(request, "POPapp/templates/index.html", context)

        """
        context['available'] = app.available()
        if not app.loaded() :
            context['loaded'] = ' '
        else :
            context['loaded'] = app.loaded()

        context['instances'] = app.instances()


        try :
            background = Background.objects.get(user=user)
        except :
            pass
        pi = PersonalInfo.objects.get(user=user)
        pi.connections = Connection.objects.filter(user=user)
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
                print request.FILES
                print request.POST
                print loadFile
                app.loadDesign(loadFile)
                request.session['application'] = pickle.dumps(app)
        elif request.POST.has_key('save_des'):
            #save_path = settings.BASE_DIR
            app.saveDesign( "design.txt")
            context['des_url'] = settings.BASE_DIR + "/design.txt"
        elif request.POST.has_key('call_method'):
            form = CallMethodForm(request.POST or None)
            if form.is_valid() :
                method = form.cleaned_data['method']
                mid = form.cleaned_data['mid']
                param0 = form.cleaned_data['param0'].split(',')
                context['callMethod'] = app.callMethod(mid,method,*param0)
                request.session['application'] = pickle.dumps(app)
        elif request.POST.has_key('execute') :
            app.execute()
            return render(request, "index2.html", context)

        
        return render(request, "POPapp/templates/index.html", context)"""
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
