from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('web.views',
	# Index
	url(r'^$', 'index', name='web.index'),
	url(r'^create_action/$', 'create_action', name='web.create_action'),
	url(r'^action/(?P<action_id>\d+)/edit/$', 'edit_action', name='web.edit_action'),
	url(r'^action/(?P<action_id>\d+)/$', 'view_action', name='web.view_action'),
	url(r'^user/(?P<user_id>\d+ )/$', 'user_page', name='web.user_page'),
	url(r'^login/$', 'login', name='web.login'),
)
