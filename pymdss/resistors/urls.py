from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name="resistors"),
    path('home', views.index, name="resistors"),
    path('selectCalibrationArea', views.selectCalibrationArea, name="selectCalibrationArea"),
    path('calibrationArea', views.calibrationArea, name="calibrationArea"),
    path('documentation', views.documentation, name='documentation'),
    path('redirect', views.redirect, name='redirect'),
    path(r'search/', views.search, name='search'),
    path(r'upload/', views.upload, name='upload'),
    path(r'process/', views.process, name='process'),
]