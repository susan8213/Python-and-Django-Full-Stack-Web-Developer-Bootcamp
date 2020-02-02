from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App </em>")

def help(request):
    context = {"insert_me": "Help PAGE"}
    return render(request, 'second_app/index.html', context=context)

def users(request):
    user_list = User.objects.all().order_by('firstname')
    context = {"user_list": user_list}
    return render(request, 'second_app/users.html', context=context)