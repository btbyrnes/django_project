from django.urls import path, register_converter
from rest_framework.authtoken.views import obtain_auth_token

from .converters import DateConverter
from .views import MenuItemView, SingleMenuItemView, ReservationView


register_converter(DateConverter, "date")


urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name="menu_items"),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name="menu_item"),
    path("reservations/", ReservationView.as_view(), name="booking"),
    path("reservations/<str:reservation_date>", ReservationView.as_view(), name="bookings_list"),
    path('api-token-auth/', obtain_auth_token),
]