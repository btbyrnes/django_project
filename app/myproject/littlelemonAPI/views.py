from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, BookingViewSerializer


class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingView(ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self, pk=None):
        queryset = Booking.objects.all()
        reservation_date = self.request.query_params.get('reservation_date')
        if reservation_date is not None:
            print(reservation_date)
            queryset = queryset.filter(reservation_date=reservation_date)
        return queryset