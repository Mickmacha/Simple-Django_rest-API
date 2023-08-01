from django.shortcuts import render
from django.http import JsonResponse
from .models import Beverages
from .serializers import BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def beverage_list(request, format=None):
    if request.method == 'GET':
        beverages = Beverages.objects.all()
        bserializer = BeverageSerializer(beverages, many=True)
        return Response(bserializer.data)
    
    elif request.method == 'POST':
        bserializer = BeverageSerializer(data=request.data)
        if bserializer.is_valid():
            bserializer.save()
            return Response(bserializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def beverage_detail(request, pk, format=None):
    try:
        beverages = Beverages.objects.get(pk=pk)
    except Beverages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        bserializer = BeverageSerializer(beverages)
        return Response(bserializer.data)
    
    elif request.method == "PUT":
        bserializer = BeverageSerializer(beverages, data=request.data)
        if bserializer.is_valid():
            bserializer.save()
            return Response(bserializer.data)
        return Response(bserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        beverages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    