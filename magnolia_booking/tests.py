import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magnolia_booking.settings')
django.setup()

from rooms.models import Room
def room_test():
    room1 = Room.objects.create(name="101", capacity=5, description="Very big room")
    print(room1.name)
    print(room1.capacity)
    print(room1.description)

def create_room(name, capacity, description):
    room = Room.objects.create(name=name, capacity=capacity, description=description)
    return room

if __name__ == "__main__":
    deluxe_apartment = {"name": "Sunset Studio",
                        "capacity": 2,
                        "description": "A cozy studio perfect for couples or close friends. Enjoy your stay in peace and comfort."}

    studio_apartment = {"name": "Sunrise Studio",
                        "capacity": 3,
                        "description": "Ideal for small families, with a comfortable layout and all the necessary amenities."}

    apartment = {"name": "Palm Retreat Apartment",
                 "capacity": 5,
                 "description": "A spacious apartment perfect for families or larger groups looking for comfort and privacy."}

    create_room(deluxe_apartment['name'], deluxe_apartment['capacity'], deluxe_apartment['description'])
    create_room(studio_apartment['name'], studio_apartment['capacity'], studio_apartment['description'])
    create_room(apartment['name'], apartment['capacity'], apartment['description'])

