from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'web.views',
    url(r'^$', 'index', name='web.index'),
	url(r'^actions/$', 'view_all_actions', name='web.view_all_actions'),
    url(r'^action/add/$', 'add_action', name='web.add_action'),
    url(r'^action/edit/(?P<action_id>\d+)/edit/$', 'edit_action', name='web.edit_action'),
    url(r'^action/(?P<action_id>\d+)/$', 'view_action', name='web.view_action'),
    url(r'^user/(?P<user>\d+)/$', 'user_page', name='web.user_page'),
)
