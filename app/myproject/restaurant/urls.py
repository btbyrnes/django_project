from django.urls import path
from .views import index, about, book, bookings, reservations
from littlelemonAPI.views import MenuItemView, SingleMenuItemView


urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('bookings/', bookings, name='bookings'), 
    path('reservations/', reservations, name="reservations"),

    path('menu/', about, name="menu"),
    
    path('menu-item/', MenuItemView.as_view()),
    path('menu-item/<int:pk>/', SingleMenuItemView.as_view()),  

]