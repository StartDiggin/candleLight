# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import User

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def create(request):
    user = User.objects.create_user(
    name=request.POST['name'],
    email=request.POST['email'],
    password=request.POST['password'],
    confirm_password=request.POST['confirm_password']
    )

    return redirect('/login')

def login(request):
    if request.POST['email']:
        user = User.objects.get(email=request.POST['email'])
        if user.password == request.POST['password']:
            request.session['id'] = user.id
            print user.id
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def speech(request):
    return render(request, 'login/speech.html');
