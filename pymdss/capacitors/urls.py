from django.urls import path
from . import views

urlpatterns = [ 
    path(r'capacitorIndex/', views.index, name="capacitorIndex"),
    path(r'capacitorCalibrationArea/', views.capacitorCalibrationArea, name="capacitorCalibrationArea"),
    #path(r'capacitors-index/', views.index, name="capacitors-index"),
]