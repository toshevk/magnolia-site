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