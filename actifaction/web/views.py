from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from api.models import ActionForm


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


@login_required
def stat_info(request):
	return render_to_response('user_page.html',
							  {'is_auth':request.user.is_authenticated()},
							  context_instance=RequestContext(request))

@login_required
def mainmenu(request):
	return render_to_response('index.html',
		{},
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


def user_page(request):   #display user page
	pass


def join_action(request): #join event
	pass


def view_action(request): #
	pass
