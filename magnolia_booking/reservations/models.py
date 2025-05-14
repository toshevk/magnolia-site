from django.core.exceptions import ValidationError
from django.db import models
from rooms.models import Room
from datetime import timedelta

# Create your models here.
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
    guest_name = models.CharField(max_length=100)
    group_size = models.IntegerField(default=1)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.check_in}: {self.guest_name} in {self.room} for {self.price}."

    def calculate_price(self):
        base_price = 25
        nights = (self.check_out - self.check_in).days

        if nights <= 0:
            return 0

        if self.check_in.month in [7,8]:
            base_price += 5

        return base_price * nights

    def clean(self):
        # Date cleanup
        if self.check_out <= self.check_in:
            raise ValidationError("Check-out date must be after the check-in date.")

        # Capacity check
        if self.room and self.group_size > self.room.capacity:
            raise ValidationError(f"{self.room.name} cannot host more than {self.room.capacity} people.")
        pass

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.calculate_price()
        super().save(*args, **kwargs)