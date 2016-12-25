from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^$', views.index, name='index'),
]
