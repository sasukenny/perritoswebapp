from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from reports.models import Reportes

from reports.serializer import ReportSerializer
# Create your views here.

class ResportesViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Reportes.objects.all()
        serializer = ReportSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        # newdata = PerritosSerializerParse(request.data)
        # print(newdata)
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        reporte = Reportes.objects.get(id=pk)
        serializer = ReportSerializer(reporte)
        return Response(serializer.data)
    
    def filter(self, request, pk=None):
        data=request.data
        print('data')
        print(data)
        perritolist = Reportes.objects.filter(owner = pk)
        serializer = ReportSerializer(perritolist, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def update(self, request, pk=None):
        reporte = Reportes.objects.get(id=pk)
        serializer = ReportSerializer(instance=reporte, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Reportes.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    