from django.db import models

from django.http import HttpResponse

def index(request):
    return HttpResponse("First App")
# Create your models here.
