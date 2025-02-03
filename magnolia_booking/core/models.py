from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=120)
    capacity = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Rooms'
        ordering = ('name','capacity',)

    def __str__(self):
        return self.name

# class Reservation(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rooms')
#     group_size = models.IntegerField()
#     check_in = models.DateField()
#     check_out = models.DateField()
#
#     def __str__(self):
#         return self.pk