from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from web.forms.action_forms import ActionForm
from django.http import Http404


def main_page(request):
	return render_to_response('pages/index.html')

def index(request):
	context = {
		'test': 'value',
		'kdojecar': 'hana'
	}
	return render_to_response(
		'pages/index.html',
		context,
		context_instance=RequestContext(request))


def login(request):
	pass


def logout(request):
	pass


def add_action(request):  ##create/edit action
   # if request.user.is_authenticated():
		actionform = ActionForm()
		context = {"actionform" : actionform}
		return render_to_response("pages/create_action.html", context,context_instance=RequestContext(request))

	#else:
	 #   return redirect("/login")


def edit_action(request): #edit existing action
	pass


def submit_action(request): #submit new action
	pass


@login_required
def user_page(request, user):
	user_profile = get_object_or_404(User, pk=user)
	return render(request, 'pages/user_page.html', {'user': user_profile})


def join_action(request): #join event
	pass


def view_action(request): #
	pass
