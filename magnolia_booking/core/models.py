from django.db import models

# Create your models here.

# class Reservation(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rooms')
#     group_size = models.IntegerField()
#     check_in = models.DateField()
#     check_out = models.DateField()
#
#     def __str__(self):
#         return self.pk