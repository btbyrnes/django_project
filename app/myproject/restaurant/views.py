from django.shortcuts import render
from .forms import BookingForm
from django.core import serializers
from datetime import datetime
from django.utils import timezone

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from api.serializers import ReservationSerializer
from api.views import ReservationView

from .models import MenuItem, Reservation

# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, "menu.html")


class BookingViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    pass


## TO DO: Add filtering by reservation date
def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    booking_json = "{'None'}"
    
    return render(request=request, template_name='bookings.html', context={"bookings":booking_json})


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


# Add your code here to create new views
def menu(request):
    menu_data = MenuItem.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = MenuItem.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


def res(request):
    return render(request, "res.html")
    

## TO DO: Return the api endpoint
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Reservation.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Reservation(
                first_name=data['first_name'],
                booking_date=timezone.now(),
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('reservation_date')
    print(date)
    bookings = Reservation.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    print(booking_json)

    return HttpResponse(booking_json, content_type='application/json')