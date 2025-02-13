from django.urls import path
from . import views

urlpatterns = [ 
    path(r'qconductance-index/', views.index, name="qconductance-index"),
    path(r'qconductanceCalibrationArea/', views.qconductanceCalibrationArea, name="qconductanceCalibrationArea"),
]