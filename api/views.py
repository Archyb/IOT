from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transport
from .serializers import TransportSerializer


@api_view(['GET', 'POST'])
def transport_view(request):
    if request.method == 'GET':
        transports = Transport.objects.all()
        serializer = TransportSerializer(transports, many=True)
        return Response(serializer.data)


from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import TransportSerializer


@api_view(['GET', 'POST'])
def transport_view(request):
    if request.method == 'GET':

        transports = Transport.objects.all()

        serializer = TransportSerializer(transports, many=True)

        return Response(serializer.data)


    elif request.method == 'POST':

        serializer = TransportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


from django.shortcuts import render

# Create your views here.
