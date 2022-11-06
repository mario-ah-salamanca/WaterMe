
import asyncio
import multiprocessing
import threading
import time

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from channels.generic.websocket import WebsocketConsumer
import json
import time
import board
import adafruit_dht

#from . import globals
#globals.initialize()

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D22)


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = {
            'text': 'PRUEBA',
            'temperature_c': temperature_c,
            'temperature_f': temperature_f,
            'humidity': humidity
        }
        self.send(json.dumps(data))

