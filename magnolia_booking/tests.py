import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magnolia_booking.settings')
django.setup()

from core.models import Room
def room_test():
    room1 = Room.objects.create(name="101", capacity=5, description="Very big room")
    print(room1.name)
    print(room1.capacity)
    print(room1.description)

if __name__ == "__main__":
    room_test()