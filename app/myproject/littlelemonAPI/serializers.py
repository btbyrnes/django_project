from rest_framework.serializers import ModelSerializer

from .models import MenuItem, Booking


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


# TO DO: Update the serializer to distplay string for date and time
class BookingViewSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["first_name", "no_of_guests", "reservation_date", "reservation_slot"]