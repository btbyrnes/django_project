from django.forms import ModelForm
from reservations.models import Reservation


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["first_name", "no_of_guests", "reservation_date", "reservation_slot"]
