from .models import Flight, Passenger, Reservation
from rest_framework import serializers
import re
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields= '__all__'
    def validate_flightNumber(self,flightNumber):
        if(re.match("^(a-zA-Zo-0)*&", flightNumber) == None):
            raise serializers.ValidationError("Invalid flight number. Please ensure the flight number is alphnumeric")
        return flightNumber



class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields= '__all__'



class ResevationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields= '__all__'