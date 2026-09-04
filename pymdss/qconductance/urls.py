from django.urls import path
from . import views

urlpatterns = [ 
    path(r'qconductance-index/', views.index, name="qconductance-index"),
    path(r'qconductanceCalibrationArea/', views.qconductanceCalibrationArea, name="qconductanceCalibrationArea"),
    path(r'qconductance-search/', views.qconductance_search, name='qconductance-search'),
    path(r'qconductance-upload/', views.qconductance_upload, name='qconductance-upload'),
]