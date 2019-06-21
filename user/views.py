from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from user.models import User


def join(request):
    user = User()
    user.email = request.POST['email']
    user.gender = request.POST['gender']
    user.name = request.POST['name']
    user.password = request.POST['password']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')


def joinform(request):
    return render(request, 'user/joinform.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def login(request):
    return render(request, 'user/loginform.html')