from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path('reserve/', views.make_reservation, name="make_reservation"),
    path('success/', views.reservation_success, name="reservation_success"),
    path('reserve/<int:pk>', views.make_reservation, name="make_reservation_select_room"),
]