from django.http import JsonResponse
from .models import Message, SensorData, Plant
from .serializers import MessageSerializer, SensorDataSerializer, PlantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
    


def index(request):
    return render(request, 'index.html')
