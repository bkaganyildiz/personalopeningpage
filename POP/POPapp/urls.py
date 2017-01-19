from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/loadcomponent$',views.load_component),
    url(r'^/$', views.index, name='index'),
    url(r'background', views.setBackground),
    url(r'edit', views.editProfile),

]
