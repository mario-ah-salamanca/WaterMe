from django.http import JsonResponse
from .models import Message, SensorData, Plant
from .serializers import MessageSerializer, SensorDataSerializer, PlantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from twilio.rest import Client

@api_view(['GET', 'POST'])
def message_list(request):
    
    if request.method == 'GET':
        log = Message.objects.all()
        serializer = MessageSerializer(log,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def sensor_data(request):
    log  = SensorData.objects.all()
    serializer = SensorDataSerializer(log, many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','POST','PUT','DELETE'])
def plant_data(request,id):
    try:
        plant = Plant.objects.get(pk=id)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method== 'DELETE':
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

import time
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D22)
def sensor(request):
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9 / 5) + 32
    humidity = dhtDevice.humidity
    data = {
        'temperature_c': temperature_c,
        'temperature_f':temperature_f,
        'humidity': humidity
    }

    if humidity > 70:
        account_sid = 'AC310882514c324de230f567a73c3c4d54'
        auth_token = '6d6e755303ece60689d5bd60cbe89416'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"I AM SATISFIED UWU",
            from_='+3197010287585',
            to='+491607070092'
        )
    elif humidity < 60:
        account_sid = 'AC33b4e34a7e5c7ea0d6c9528b349d9cc8'
        auth_token = 'be23ba82eb617c3d17a3839ae0829c82'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"PLEASE BRO IM DYING!",
            from_='+3197010287585',
            to='+491607070092'
        )

    return render(request, "index.html", data )