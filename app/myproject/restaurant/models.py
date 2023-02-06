from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=1)
    booking_date = models.DateTimeField()

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
   inventory = models.SmallIntegerField(default=0)

   def __str__(self):
      return self.title