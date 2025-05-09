import os
import django

from django.test import TestCase
from .models import Room, Reservation
from django.utils import timezone

class RoomTestCase(TestCase):
    rooms = None
    def setUp(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magnolia_booking.settings')
        django.setup()
        self.rooms = Room.objects.all()


    # def test_create_room(self):
    #     room1 = Room.objects.create(name="105", capacity=6, description="Even bigger room")
    #     room_name_label = room1._meta.get_field('name').max_length
    #     self.assertEqual(room_name_label, 120)
    #
    # def test_expected_room_name(self):
    #     room1 = Room.objects.create(name="106", capacity=3, description="Medium sized room")
    #     expected_room_name = "106"
    #     expected_room_description = "Medium sized room"
    #     self.assertContains(str(room1), expected_room_name)
    #
    # def test_expected_room_description(self):
    #     room1 = Room.objects.create(name="110", capacity=2, description="Lovely room for 2")
    #     expected_room_description = "Lovely room for 2"
    #     self.assertEqual(room1.description, expected_room_description)

    def print_room(self):
        room = self.rooms[0]
        print(room)