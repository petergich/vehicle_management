from django.db import models
import time
import datetime
from django.core.validators import MinValueValidator


class Driver(models.Model):
    name = models.CharField(max_length=50, unique=True)
    Driver_license_number = models.CharField(max_length=50)
    LNO_expiry_date = models.DateField()
    categories_approved = models.CharField(max_length=254)
    training = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Aprover(models.Model):
    name = models.CharField(max_length=50)
    Aprover_id = models.IntegerField()

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    Plate_no = models.CharField(max_length=20, unique=True)
    vehicle_make = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    telephone = models.IntegerField()
    Insuarance_start_date = models.DateField()
    Insuarance_expiry_date = models.DateField()
    last_inspection_date = models.DateField()
    next_inspection_date = models.DateField()
    last_service_distance = models.IntegerField()
    Distance_remaining = models.IntegerField(default=5000)
    odometer = models.IntegerField(default=0)
    expected_efficiency=models.IntegerField()
    def __str__(self):
        return self.Plate_no


class Journey(models.Model):
    Date = models.DateField()
    Driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    Start_odometer_reading = models.IntegerField(
        validators=[MinValueValidator(0)])
    Stop_odometer_reading = models.IntegerField(
        validators=[MinValueValidator(0)])
    vehicle_condition = models.CharField(max_length=50)
    initial_JMP = models.TimeField()
    final_JMP = models.TimeField()
    start_trip = models.CharField(max_length=100)
    stop_trip = models.CharField(max_length=254)
    destination = models.CharField(max_length=300)
    Approver = models.ForeignKey(Aprover, on_delete=models.SET_NULL, null=True)
    passengers = models.CharField(max_length=254)
    class meta:
        unique_together=['Date','Vehicle']

    def __str__(self):
        return str(self.Date) + " " + str(self.Vehicle)


class Fuel(models.Model):
    Date = models.DateField()
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    current_odometer_reading = models.IntegerField()
    total_distance_from_previous_fueling = models.IntegerField()
    Liters_taken = models.IntegerField()
    cost = models.IntegerField()
    effiency = models.IntegerField()
    variation = models.IntegerField()

    def __str__(self):
        return str(self.Date) + " " + str(self.Vehicle)


class Tracking(models.Model):
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Date = models.DateField()
    Daily_vehicle_tracking_distance = models.IntegerField()
    Overspeeding = models.CharField(max_length=200)
    JMP_daily_distance = models.IntegerField()

    def __str__(self):
        return str(self.Date) + " " + str(self.Vehicle)


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
