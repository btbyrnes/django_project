from django.test import TestCase
from django.test import Client
from rest_framework import status
from rest_framework.reverse import reverse

from restaurant.models import MenuItem
from api.views import MenuItemView
from api.serializers import MenuItemSerializer


client = Client()

TEST_ITEMS = [
    {
        "title":"Pizza",
        "price":5.00,
        "inventory":10,
    },
    {
        "title":"Hamburger",
        "price":10.00,
        "inventory":15,
    },
    {
        "title":"Soda",
        "price":2.00,
        "inventory":30,
    },
]


class MenuViewTest(TestCase):
    def setup(self):
        for item in TEST_ITEMS:
            title = item["title"]
            price = item["price"]
            inventory = item["inventory"]
            MenuItem.objects.create(title=title, price=price, inventory=inventory)


    def test_get_items(self):
        response = client.get(reverse('api:menu-items'))
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
