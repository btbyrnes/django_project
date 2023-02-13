from django.db import models


class MenuItem(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
   inventory = models.SmallIntegerField(default=0)

   def __str__(self):
      return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=1)
    booking_date = models.DateTimeField()
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name
