from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from perritos.models import Perrito
from perritos.serializer import PerritosSerializer, PerritosSerializerParse
# Create your views here.
class PerritosViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Perrito.objects.all()
        serializer = PerritosSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        # newdata = PerritosSerializerParse(request.data)
        # print(newdata)
        serializer = PerritosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Perrito.objects.get(id=pk)
        serializer = PerritosSerializer(product)
        return Response(serializer.data)
    
    def filter(self, request, pk=None):
        data=request.data
        print('data')
        print(data)
        perritolist = Perrito.objects.filter(owner = pk)
        serializer = PerritosSerializer(perritolist, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Perrito.objects.get(id=pk)
        serializer = PerritosSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Perrito.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
