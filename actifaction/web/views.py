from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
	return render_to_response('pages/index.html')

def login(request):
    pass

def logout(request):
    pass

def create_action(request):  ##create/edit action
    pass

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
