from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>First App</em>")
# Create your views here.
