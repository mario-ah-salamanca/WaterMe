import asyncio
import multiprocessing
import threading
import time

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

import time
import board
import adafruit_dht

#from . import globals
#globals.initialize()

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D22)


def index(request):
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9 / 5) + 32
    humidity = dhtDevice.humidity

    data = {
        'temperature_c': temperature_c,
        'temperature_f': temperature_f,
        'humidity': humidity
    }
    return render(request, 'web_page.html', data)
