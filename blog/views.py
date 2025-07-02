from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_blog(request):
    return HttpResponse("<h1>Welcome to the Blog!</h1>")