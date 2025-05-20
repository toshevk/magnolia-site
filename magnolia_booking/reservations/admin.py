from django.contrib import admin
from .models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("check_in", "guest_name", "group_size", "room", "price", "created_on",)
    list_filter = ("check_in", "room", "guest_name", "created_on",)

admin.site.register(Reservation, ReservationAdmin)