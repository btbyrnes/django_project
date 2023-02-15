from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from .models import Reservation
from .serializers import ReservationSerializer

# Create your views here.
class ReservationView(ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self, pk=None):
        queryset = Reservation.objects.all()
        reservation_date = self.request.query_params.get('reservation_date')
        if reservation_date is not None:
            print(reservation_date)
            queryset = queryset.filter(reservation_date=reservation_date)
        return queryset


class ReservationListView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    

class BReservationCreateView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
