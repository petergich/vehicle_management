
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
        passw = request.POST['passw']

        user = auth.authenticate(username=usern, password=passw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in ' + usern)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Dashboard Module
@login_required(login_url="")
def Dashboard(request):
    return render(request, 'index.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')


@login_required(login_url="")
def journey(request):
    if request.method == 'POST':
        date = request.POST['date']
        driver = request.POST['nam']
        vehicles = request.POST['vehicle']
        stop = request.POST['stop']
        vehicle_condition = request.POST['vehicle_condition']
        initial_jmp = request.POST['initial_jmp']
        final_jmp = request.POST['final_jmp']
        start_trip = request.POST['start_trip']
        destination = request.POST['destination']
        stop_trip = request.POST['stop_trip']
        trip_approved = request.POST['trip_approved']
        passengers = request.POST['passengers']
        veh = Vehicle.objects.get(Plate_no=vehicles)
        dr = Driver.objects.get(name=driver)
        app = Aprover.objects.get(name=trip_approved)
        start = veh.odometer
        if int(stop) <= start:
            vehicles = Vehicle.objects.all()
            drivers = Driver.objects.all()
            aprovers = Aprover.objects.all()
            return render(request, 'addjmp.html', {"vehicles": vehicles, "drivers": drivers, "aprovers": aprovers, "message": "The odometer reading you entered is less or equal to the existing odometer reading"})

        instance = Journey(Date=date, Driver=dr, Vehicle=veh, Start_odometer_reading=start, Stop_odometer_reading=stop, vehicle_condition=vehicle_condition,
                           initial_JMP=initial_jmp, final_JMP=final_jmp, start_trip=start_trip, stop_trip=stop_trip, destination=destination, Approver=app, passengers=passengers)
        veh.odometer = int(stop)
        change = int(stop) - start
        dist = veh.Distance_remaining - change
        if dist < 0:
            veh.Distance_remaining = 0
        else:
            veh.Distance_remaining = dist

        try:
            veh.save()
            instance.save()
            vehicles = Vehicle.objects.all()
            drivers = Driver.objects.all()
            aprovers = Aprover.objects.all()
            return render(request, 'addjmp.html', {"vehicles": vehicles, "drivers": drivers, "aprovers": aprovers, "message": "Saved Successfully"})
        except:
            vehicles = Vehicle.objects.all()
            drivers = Driver.objects.all()
            aprovers = Aprover.objects.all()
            return render(request, 'addjmp.html', {"vehicles": vehicles, "drivers": drivers, "aprovers": aprovers, "message": "Error Occured"})
    else:
        vehicles = Vehicle.objects.all()
        drivers = Driver.objects.all()
        aprovers = Aprover.objects.all()
        return render(request, 'addjmp.html', {"vehicles": vehicles, "drivers": drivers, "aprovers": aprovers})


@login_required(login_url="")
def vehicle(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehiclemanagement.html", {"vehicles": vehicles})


@login_required(login_url="")
def fuel(request):
    if request.method == "POST":
        date = request.POST['date']
        vehicles = request.POST['vehicle']
        driver = request.POST['driver']
        current_odometer_reading = request.POST['current_odometer_reading']
        liters_taken = request.POST['liters_taken']
        cost = request.POST['cost']
        veh = Fuel.objects.filter(Vehicle__Plate_no=vehicles)
        dr = Driver.objects.get(name=driver)
        dte = []
        vehic = Vehicle.objects.get(Plate_no=vehicles)
        if veh:
          for i in veh:
            dte.append(i.Date)
          vehi = Fuel.objects.get(Vehicle__Plate_no=vehicles, Date=max(dte))
          tot = int(current_odometer_reading) - int(vehi.current_odometer_reading)
          eff = tot / vehi.Liters_taken
          vari = vehic.expected_efficiency - eff
        else:
            eff=vehic.expected_efficiency
            tot=0
            vari=0
        vehicles = Vehicle.objects.all()
        drivers = Driver.objects.all()
        fuels = Fuel.objects.all()
        instance = Fuel(Date=date, Vehicle=vehic, Driver=dr, current_odometer_reading=current_odometer_reading,
                    total_distance_from_previous_fueling=tot, Liters_taken=liters_taken, cost=cost, effiency=eff, variation=vari)
        try:
            instance.save()
            vehicles = Vehicle.objects.all()
            drivers = Driver.objects.all()
            fuels = Fuel.objects.all()
            return render(request, "fuel.html", {"fuels": fuels, "vehicles": vehicles, "drivers": drivers, "message": "Saved Successfully"})
        except:
            vehicles = Vehicle.objects.all()
            drivers = Driver.objects.all()
            fuels = Fuel.objects.all()
            return render(request, "fuel.html", {"fuels": fuels, "vehicles": vehicles, "drivers": drivers, "message": "Error Occured"})
    else:
        vehicles = Vehicle.objects.all()
        drivers = Driver.objects.all()
        fuels = Fuel.objects.all()
        return render(request, "fuel.html", {"fuels": fuels, "vehicles": vehicles, "drivers": drivers})

# Create your views here.


@login_required(login_url="")
def tracking(request):
    if request.method == "POST":
        vehicle = request.POST['vehicle']
        driver = request.POST['driver']
        date = request.POST['date']
        daily_distance = request.POST['distance']
        overspeeding = request.POST['speeding']
        jmp_daily_distance = request.POST['jmpdistance']
        veh = Vehicle.objects.get(Plate_no=vehicle)
        dr = Driver.objects.get(name=driver)
        instance = Tracking(Vehicle=veh, Driver=dr, Date=date, Daily_vehicle_tracking_distance=daily_distance,
                            Overspeeding=overspeeding, JMP_daily_distance=jmp_daily_distance)
        try:
            instance.save()
        except:
            HttpResponse("Unable to save")
    else:
        vehicles = Vehicle.objects.all()
        drivers = Driver.objects.all()
        return render(request, 'tracking.html', {"vehicles": vehicles, "drivers": drivers})
