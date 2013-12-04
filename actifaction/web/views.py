from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from api.models import ActionForm

def main_page(request):
	return render_to_response('pages/index.html')

def index(request):
    context = {'test': 'value'}
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


def user_page(request):   #display user page
    pass


def join_action(request): #join event
    pass


def view_action(request): #
    pass
