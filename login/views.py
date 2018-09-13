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
