from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from restaurant.models import MenuItem, Reservation

from .serializers import MenuItemSerializer, ReservationSerializer

@api_view()
@permission_classes([IsAuthenticated])
def message(request):
    return Response({"message":"This view is protected"})


class MenuItemView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        request = self.request
        queryset = Reservation.objects.all()
        reservation_date = request.query_params.get("reservation_date")
        if reservation_date is not None:
            queryset = queryset.filter(reservation_date=reservation_date)
        return queryset

