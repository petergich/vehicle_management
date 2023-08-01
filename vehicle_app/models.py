from django.db import models
import time
import datetime
from django.core.validators import MinValueValidator

class Driver(models.Model):
    name=models.CharField(max_length=50)
    Driver_id=models.IntegerField()
    def __str__(self):
        return self.name
class Aprover(models.Model):
    name=models.CharField(max_length=50)
    Aprover_id=models.IntegerField()
    def __str__(self):
        return self.name
class Vehicle(models.Model):
    Plate_no=models.CharField(max_length=20)
    Insuarance_start_date=models.DateField()
    Insuarance_expiry_date=models.DateField()
    last_inspection_date=models.DateField()
    next_inspection_date=models.DateField()
    last_service_distance=models.IntegerField() 
    Distance_remaining=models.IntegerField(default=100000)
    odometer=models.IntegerField(default=0)
    def __str__(self):
        return self.Plate_no
class Journey(models.Model):
    Date=models.DateField()
    Driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True)
    Vehicle=models.ForeignKey(Vehicle, on_delete=models.SET_NULL,null=True)
    Start_odometer_reading=models.IntegerField(validators=[MinValueValidator(0)])
    Stop_odometer_reading=models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_condition=models.CharField(max_length=50)
    initial_JMP=models.TimeField()
    final_JMP=models.TimeField()
    start_trip=models.CharField(max_length=100)
    stop_trip=models.CharField(max_length=254)
    destination=models.CharField(max_length=100)
    Approver=models.ForeignKey(Aprover,on_delete=models.SET_NULL,null=True)
    passengers=models.CharField(max_length=254)
    def __str__(self):
        return self.date

