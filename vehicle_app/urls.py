from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Login, name="login"),
    path("", views.Logout, name='logout'),
    path("dashboard", views.Dashboard, name="dashboard"),
    path('journey', views.journey, name="journey"),
    path('vehicle', views.vehicle, name='vehicle'),
    path('fuel', views.fuel, name='fuel'),
    path('tracking', views.tracking, name='tracking'),
    path('vehiclemaintenance', views.vehiclemaintenance, name='vehiclemaintenance'),
    path('vehicleinspection', views.vehicleinspection, name='vehicleinspection'),
    path('vehicleinsuarance', views.vehicleinsuarance, name='vehicleinsuarance'),
    path('vehicleservicing', views.vehicleservicing, name='vehicleservicing'),
    path('fuelingreport', views.fuelingreport, name='fuelingreport'),
    path('jmpreports', views.jmpreports, name='jmpreports'),
    path('trackingreports', views.trackingreports, name='trackingreports'),
]
