from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from restaurant.models import MenuItem, Reservation

from .serializers import MenuItemSerializer, ReservationSerializer


class MenuItemView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class ReservationView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        request = self.request
        queryset = Reservation.objects.all()
        reservation_date = request.query_params.get("reservation_date")
        if reservation_date is not None:
            queryset = queryset.filter(reservation_date=reservation_date)
        return queryset

