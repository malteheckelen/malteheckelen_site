from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

def index(request):
    return(render(request, 'helpmeout/index.html'))

def index_de(request):
    return(render(request, 'helpmeout/index.de.html'))

def callback(request):
    return(render(request, 'helpmeout/callback.html'))
