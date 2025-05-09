from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('all/', views.room_list, name='room-list'),
]