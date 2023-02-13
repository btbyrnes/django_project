from django.forms import ModelForm
from littlelemonAPI.models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["first_name", "no_of_guests", "reservation_date", "reservation_slot"]
