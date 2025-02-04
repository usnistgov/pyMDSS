from django.shortcuts import render
from time import sleep
from .tasks import go_to_sleep

# Create your views here.
def index(request):
    go_to_sleep.delay(5)
    return render(request, 'capacitors-index.html')

def capacitor_calibrationArea(request):
    return render(request, 'capacitorCalibrationArea.html')

def quantum_calibrationArea(request):
    return render(request, 'quantum_calibrationArea.html')