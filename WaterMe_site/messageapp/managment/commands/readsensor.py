# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from channels import Group
from django.core.management import BaseCommand
import time
import board
import adafruit_dht
import globals


# Initial the dht device, with data pin connected to:

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Reading sensor and sending over Channel."
    dhtDevice = adafruit_dht.DHT11(board.D22)

    # A command must define handle()
    def handle(self, *args, **options):
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        globals.data['temperature_c'] = 50.0
        globals.data['temperature_f'] = 50.0
        globals.data['humidity'] = 50.0
        while True:
            data =  "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity)
            Group("sensor").send(data)
            time.sleep(2)
            x = x + 1
            self.stdout.write("Sensor reading..." + data)

