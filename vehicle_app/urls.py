from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Login, name="login"),
    path("dashboard", views.Dashboard, name="dashboard"),
    path('journey', views.journey, name="journey"),
    path('vehicle', views.vehicle, name='vehicle'),
    path('fuel', views.fuel, name='fuel'),
    path('tracking', views.tracking, name='tracking'),
]
