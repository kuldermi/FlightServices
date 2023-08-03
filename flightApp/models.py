from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length = 20)
    operatingAirlines = models.CharField ( max_length = 20 )
    departureCity = models.CharField ( max_length = 20, blank= True )
    arrivalCity = models.CharField ( max_length = 20 )
    dateOfDeparture = models.DateField()
    estimatedDepartureTime = models.TimeField()



class Passenger(models.Model):
    firstName = models.CharField(max_length= 20)
    lastName = models.CharField(max_length= 20)
    age= models.IntegerField()
    email= models.EmailField()
    phoneNumber= models.CharField(max_length = 13)
class Reservation(models.Model):
    flight= models.ForeignKey(Flight, on_delete = models.CASCADE)
    passenger= models.OneToOneField(Passenger, on_delete = models.CASCADE)