from django.urls import path

from .consumers import WSConsummer

ws_urlpattern =[
    path('ws/humidity-temperature/',WSConsummer.as_asgi())
]