from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.
class Bike(models.Model):
    STANDARD, TANDEM, ELECTRIC = "ST", "TA", "EL"
    BIKE_TYPE_CHOICES = [(STANDARD, "Standard"), (TANDEM, "Tandem"), (ELECTRIC, "Electric") ]
    bike_type = models.CharField(max_length = 2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    color = models.CharField(max_length = 10, default="")
    def __str__(self):
        return self.bike_type + " - " + self.color
class Renter(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)
    vip_num = models.IntegerField(default = 0)
    def __str__(self):
        return self.first_name + " " + self.last_name + " - #" + self.phone

class Rental(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0)

    def calc_price(self):
        curr_price = BASE_PRICE
        if self.bike.bike_type == "TA":
            curr_price += TANDEM_SURCHARGE
        
        if self.bike.bike_type == "EL":
            curr_price += ELECTRIC_SURCHARGE

        if self.renter.vip_num > 0:
            curr_price *= 0.8 
        self.price = curr_price

bike1 = Bike(bike_type="ST", color="purple")      
bike1.save()
bike2 = Bike(bike_type="TA", color="blue")      
bike2.save()
bike3 = Bike(bike_type="EL", color="orange")      
bike3.save()
bike4 = Bike(bike_type="ST", color="green")      
bike4.save()
bike5 = Bike(bike_type="EL", color="red")      
bike5.save()

renter1 =Renter(first_name = "Klinsmann", last_name = "Agyei", phone = "0203980856", vip_num = 3)
renter1.save()
renter2 =Renter(first_name = "Kwabena", last_name = "Amo", phone = "045788432", vip_num = 2)
renter2.save()
renter3 =Renter(first_name = "Amalitech", last_name = "Trainee", phone = "0303980856", vip_num = 1)
renter3.save()

first_bike = Bike.objects.first()
first_renter = Renter.objects.first()
example_rental = Rental(bike=first_bike, renter=first_renter)
example_rental.save()

Renter.objects.filter(first_name = "Klinsmann")