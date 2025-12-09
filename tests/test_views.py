from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Burger", price=10.50, inventory=50)
        self.menu2 = Menu.objects.create(title="Pizza", price=15.00, inventory=30)
        self.menu3 = Menu.objects.create(title="Pasta", price=12.75, inventory=40)

    def test_getall(self):
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data

        self.assertEqual(len(serialized_data), 3)
        self.assertEqual(serialized_data[0]["title"], "Burger")
        self.assertEqual(float(serialized_data[0]["price"]), 10.50)
        self.assertEqual(serialized_data[1]["title"], "Pizza")
        self.assertEqual(float(serialized_data[1]["price"]), 15.00)
        self.assertEqual(serialized_data[2]["title"], "Pasta")
        self.assertEqual(float(serialized_data[2]["price"]), 12.75)
