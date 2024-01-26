from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Salad", price=50, inventory=10)
        Menu.objects.create(title="Tomato Pasta", price=160, inventory=1)

    def test_getall(self):
        url = 'http://localhost:8000/restaurant/menu'
        response = self.client.get(url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
