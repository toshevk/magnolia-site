from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=120)
    capacity = models.IntegerField()
    description = models.TextField()
    layout = models.TextField()
    bed_configuration = models.TextField()
    amenities = models.TextField()

    class Meta:
        verbose_name_plural = 'Rooms'
        ordering = ('name','capacity',)

    def __str__(self):
        return f"{self.name}, fits {self.capacity} guests."

class Reservation(models.Model):
    reserved_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_email = models.EmailField()
    number_of_guests = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation {self.pk}: {self.guest_email} reserved {self.reserved_room.name} for {self.number_of_guests}."

    def save(self, *args, **kwargs):
        if self.check_in_date < timezone.now().date():
            raise ValidationError("You cannot reserve in the past!")
        super(Reservation, self).save(*args, **kwargs)

if __name__ == "__main__":
    rooms = Room.objects.all()
    print(rooms)