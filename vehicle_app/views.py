
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.shortcuts import render, redirect
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
import os
import time
import datetime



from django.contrib.auth.decorators import login_required


def Login(request):
    if request.method == 'POST':
        usern = request.POST['usern']
        passw = request.POST['pas']

        user = auth.authenticate(username=usern, password=passw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in ' + usern)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Login')
    else:
        return render(request, 'login.html')


# Dashboard Module
@login_required(login_url="/login/")
def Dashboard(request):
    return render(request,'index.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')
def journey(request):
    return render(request,'addjmp.html')

def vehicle(request):
    vehicles=Vehicle.objects.all()
    return render(request,"vehiclemanagement.html",{"vehicles":vehicles})
# Create your models here.


# Create your views here.
