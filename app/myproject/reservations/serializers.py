from rest_framework.serializers import ModelSerializer

from .models import Reservation


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


# TO DO: Update the serializer to display string for date and time
class ReservationViewSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["first_name", "no_of_guests", "reservation_date", "reservation_slot"]