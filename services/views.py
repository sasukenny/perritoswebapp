from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from services.models import hired_service, service

from services.serializer import HiredServiceSerializer, ServiceSerializer
# Create your views here.
class ServiciosViewSet(viewsets.ModelViewSet):
    def list(self, request):
        servicelist = service.objects.all()
        serializer = ServiceSerializer(servicelist, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        serviceitem = service.objects.get(id=pk)
        serializer = ServiceSerializer(serviceitem)
        return Response(serializer.data)
    
    def filter(self, request, pk=None):
        servicelist = service.objects.filter(id = pk)
        serializer = ServiceSerializer(servicelist)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serviceitem = service.objects.get(id=pk)
        serializer = ServiceSerializer(instance=serviceitem, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        serviceitem = service.objects.get(id=pk)
        serviceitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ServicioContratadoViewSet(viewsets.ModelViewSet):
    def list(self, request):
        hired_serviceList = hired_service.objects.all()
        serializer = HiredServiceSerializer(hired_serviceList, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = HiredServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        hired_serviceItem = hired_service.objects.get(id=pk)
        serializer = HiredServiceSerializer(hired_serviceItem)
        return Response(serializer.data)
    
    def filter(self, request, pk=None):
        data=request.data
        perritodata= data.get('perrito')
        hired_serviceList = hired_service.objects.filter(perrito = perritodata)
        serializer = HiredServiceSerializer(hired_serviceList)
        return Response(serializer.data)

    def update(self, request, pk=None):
        hired_serviceItem = hired_service.objects.get(id=pk)
        serializer = HiredServiceSerializer(instance=hired_serviceItem, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        hired_serviceItem = hired_service.objects.get(id=pk)
        hired_serviceItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PerritoServicioContratadoViewSet(viewsets.ModelViewSet):
    def filter(self, request, pk=None):
        data=request.data
        perritodata= data.get('perrito')
        hired_serviceList = hired_service.objects.filter(perrito = pk)
        serializer = HiredServiceSerializer(hired_serviceList, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        hired_serviceItem = hired_service.objects.get(id=pk)
        serializer = HiredServiceSerializer(instance=hired_serviceItem, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        hired_serviceItem = hired_service.objects.get(id=pk)
        hired_serviceItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)