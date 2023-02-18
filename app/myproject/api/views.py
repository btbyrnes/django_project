from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission

from restaurant.models import MenuItem, Reservation

from .serializers import MenuItemSerializer, ReservationSerializer


SAFE_METHODS = ["GET"]
class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if ((request.method in SAFE_METHODS) or (request.user.is_authenticated)):
            return True
        else:
            return False


@api_view()
@permission_classes([IsAuthenticated])
def message(request):
    return Response({"message":"This view is protected"})


class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class ReservationView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        request = self.request
        queryset = Reservation.objects.all()
        reservation_date = request.query_params.get("reservation_date")
        if reservation_date is not None:
            queryset = queryset.filter(reservation_date=reservation_date)
        return queryset

