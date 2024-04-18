import random

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from flights.models import Flight, User
from flights.serializers import FlightSerializer


# Create your views here.
class FlightViewSet(viewsets.ViewSet):
    def list(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        flight = Flight.objects.get(id=pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    def update(self, request, pk=None):
        flight = Flight.objects.get(id=pk)
        serializer = FlightSerializer(instance=flight, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        flight = Flight.objects.get(pk=pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({'id': user.id})