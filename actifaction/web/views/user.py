"""
User handling views
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext
from api.models import UserProfile, Action

from web.forms.user_forms import UserCreateForm, UserProfileForm
from web.forms.user_forms import UserAlreadyExistsError

from web.processors import get_user, get_user_profile
from web.processors import create_or_update_profile


def register_user(request):
	form = UserCreateForm()

	if request.method == 'POST':
		form = UserCreateForm(request.POST)

	if form.is_valid():
		try:
			user = form.save()
			user = authenticate(username=request.POST['email'],
			                    password=request.POST['password1'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('user_page', args=[user.pk]))

		except UserAlreadyExistsError:
			messages.error(request, 'Uporabnik s tem emailom ze obstaja')

	return render_to_response(
		'registration/register_user.html', {
		'form': form,
		},
		context_instance=RequestContext(request))


@login_required
def user_page(request, user_id):
	user = get_user(user_id)
	all_actions = Action.objects.filter(organizer=user)
	user_profile = get_user_profile(user_id)
	return render_to_response(
		'pages/user_page.html', {
		'user': user,
		'user_profile': user_profile,
		'actions': all_actions,
		},
		context_instance=RequestContext(request))


@login_required
def user_profile(request, user_id):
	profile = get_user_profile(user_id)
	if profile:
		form = UserProfileForm(initial=profile.__dict__)
	else:
		form = UserProfileForm()

	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
	if form.is_valid():
		# user profile create or update
		user_data = {}
		user_data.update(form.cleaned_data)

		profile = create_or_update_profile(user_id, **user_data)

	return render_to_response('registration/user_profile.html', {
		'form': form,
	    'profile': profile,
	}, context_instance=RequestContext(request))


