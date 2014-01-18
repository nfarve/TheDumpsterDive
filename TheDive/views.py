from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Dumpster Dive")


