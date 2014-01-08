from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.forms.login_form import LoginForm
admin.autodiscover()

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	# WEB
	(r'', include('web.urls')),

	# ADMIN
	url(r'^admin/', include(admin.site.urls)),

	# STATIC CONTENT
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

urlpatterns += patterns(
	'',
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',
	    {'template_name': 'registration/login.html', 'authentication_form': LoginForm},
	    name='login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
	    {'next_page': '/'}, name='logout'),
	url(r'^accounts/register/$', 'web.views.user_register',
	    name='register')
)

