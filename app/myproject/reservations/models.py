from django.db import models


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=1)
    booking_date = models.DateTimeField()
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name