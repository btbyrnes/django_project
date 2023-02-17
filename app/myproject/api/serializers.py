from rest_framework.serializers import ModelSerializer

from restaurant.models import MenuItem
from restaurant.models import Reservation


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"