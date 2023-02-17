from django.urls import path, register_converter
from rest_framework.authtoken.views import obtain_auth_token

from .converters import DateConverter
from .views import MenuItemView, SingleMenuItemView, ReservationView


register_converter(DateConverter, "date")

app_name = "api"

urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name="menu_items"),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name="menu_item"),
    path("reservations/", ReservationView.as_view(), name="reservations"),
    path("reservations/<str:reservation_date>", ReservationView.as_view(), name="reservations"),
    path('api-token-auth/', obtain_auth_token),
]