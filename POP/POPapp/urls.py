from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/loadcomponent$', views.load_component),
	url(r'^/addinstance$', views.add_instance),
	url(r'^/removeinstance$', views.remove_instance),
	url(r'^/callmethod$', views.call_method),
	url(r'^/execute$', views.execute),
	url(r'^/?$', views.index, name='index'),
	url(r'background', views.setBackground),
	url(r'edit', views.editProfile),
	url(r'sesdel', views.deleteSession),
]
