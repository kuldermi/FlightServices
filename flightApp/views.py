from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ResevationSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity= request.data["departureCity"], arrivalCity= request.data["arrivalCity"], dateOfDeparture= request.data["dateOfDeparture"])
    serializer = FlightSerializer(flights, many = True)
    return Response(serializer.data)
@api_view(['POST'])
def save_passenger(request):
    try:
        flight= Flight.objects.get(id= request.data['flightId'])
    except:
        Response(status = status.HTTP_400_BAD_REQUEST)
    else:
        Response(status= status.HTTP_400_BAD_REQUEST)


    passenger= Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.age = request.data['age']
    passenger.email = request.data['email']
    passenger.phoneNumber = request.data['phoneNumber']
    passenger.save()

    reservation= Reservation()
    reservation.flight= flight
    reservation.passenger = passenger
    reservation.save()
    return Response(status = status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ResevationSerializer

