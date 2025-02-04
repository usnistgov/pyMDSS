from django.urls import path
from . import views

urlpatterns = [ 
    path(r'capacitors-index/', views.index, name="capacitors-index"),
    path(r'capacitor_calibrationArea/', views.capacitor_calibrationArea, name="capacitor_calibrationArea"),
    #path(r'capacitors-index/', views.index, name="capacitors-index"),
]