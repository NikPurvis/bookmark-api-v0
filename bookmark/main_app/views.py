# main_app/views.py

# Import dependencies
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Welcome</h1>')
