import os
import django
from datetime import datetime, timedelta
from restaurant.models import Menu, Booking

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
django.setup()

# Clear existing data (optional)
Menu.objects.all().delete()
Booking.objects.all().delete()

# Add sample Menu items
menu_items = [
    {"title": "Pasta Carbonara", "price": 12.99, "inventory": 50},
    {"title": "Pizza Margherita", "price": 15.50, "inventory": 40},
    {"title": "Caesar Salad", "price": 8.99, "inventory": 60},
    {"title": "Grilled Salmon", "price": 24.99, "inventory": 25},
    {"title": "Chocolate Cake", "price": 6.99, "inventory": 30},
]

for item in menu_items:
    menu = Menu.objects.create(**item)
    print(f"Created Menu: {menu.title} - ${menu.price}")

# Add sample Booking records
now = datetime.now()
bookings = [
    {
        "name": "John Doe",
        "no_of_guests": 4,
        "booking_date": now + timedelta(days=7, hours=19),
    },
    {
        "name": "Jane Smith",
        "no_of_guests": 2,
        "booking_date": now + timedelta(days=8, hours=20),
    },
    {
        "name": "Michael Johnson",
        "no_of_guests": 6,
        "booking_date": now + timedelta(days=9, hours=18),
    },
    {
        "name": "Sarah Williams",
        "no_of_guests": 3,
        "booking_date": now + timedelta(days=10, hours=19, minutes=30),
    },
    {
        "name": "Robert Brown",
        "no_of_guests": 5,
        "booking_date": now + timedelta(days=11, hours=20),
    },
]

for booking in bookings:
    new_booking = Booking.objects.create(**booking)
    print(
        f"Created Booking: {new_booking.name} - {new_booking.no_of_guests} guests on {new_booking.booking_date}"
    )

print("\n✅ Sample data added successfully!")
