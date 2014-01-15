from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views.user import register_user
from web.views.user import user_profile
from web.views.user import user_page

from web.forms.user_forms import LoginForm
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
	url(r'^accounts/register/$', register_user, name='register'),
    url(r'^accounts/user_profile/(?P<user_id>\d+)/$', user_profile, name='user_profile'),
    url(r'^accounts/(?P<user_id>\d+)/$', user_page, name='user_page'),
)

