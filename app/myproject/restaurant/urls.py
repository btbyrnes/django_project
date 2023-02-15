from django.urls import path, include
from .views import index, about, book, bookings, reservations
from littlelemonAPI.views import MenuItemView, SingleMenuItemView
from littlelemonAPI.views import ReservationView


urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('bookings/', bookings, name='bookings'),
    path('reservations/', ReservationView.as_view(), name="reservations", kwargs={"format":"json"}),

    path('menu/', about, name="menu"),
    
    path('menu-item/', MenuItemView.as_view()),
    path('menu-item/<int:pk>/', SingleMenuItemView.as_view()),  

    # The API Endpoints
    path("api/", include("littlelemonAPI.urls"), kwargs={"format":"json"}),
]