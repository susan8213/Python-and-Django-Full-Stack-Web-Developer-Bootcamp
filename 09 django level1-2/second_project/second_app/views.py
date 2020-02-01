from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App </em>")

def help(request):
    context = {"insert_me": "Help PAGE"}
    return render(request, 'second_app/index.html', context=context)