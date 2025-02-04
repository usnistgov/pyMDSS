from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('selectCalibrationArea/', views.selectCalibrationArea, name='selectCalibrationArea'),
    path('calibrationArea/', views.calibrationArea, name='calibrationArea'),
    path('documentation/', views.documentation, name='documentation'),
    path('redirect', views.redirect, name='redirect'),
    path(r'search/', views.search, name='search'),
    path(r'upload/', views.upload, name='upload'),
    path(r'process/', views.process, name='process'),
    path('check_task_status/<task_id>/', views.get_task_status, name='check_task_status'),
]