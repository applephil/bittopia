from django.shortcuts import render

# Create your views here.

def index(request):
	return HttpResponse("Hello, testing")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s, whose name is %s." % (user_id, user_name))