from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path('request_room/search/', views.booking_search, name="booking_search"),
    path('request_room/results/', views.booking_result, name="booking_result"),
    path('reserve/', views.make_reservation, name="make_reservation"),
    path('success/', views.reservation_success, name="reservation_success"),
    path('reserve/<int:pk>', views.make_reservation, name="make_reservation_select_room"),
]