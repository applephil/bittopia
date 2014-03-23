
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'bittopia/index.html', {})
#return HttpResponse("Front page + login screen")

def signup(request):
    return HttpResponse('signup page')


