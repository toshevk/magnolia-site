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


if __name__ == "__main__":
    rooms = Room.objects.all()
    print(rooms)