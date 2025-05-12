from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('all/', views.room_list, name='room-list'),
    path('detail/<int:room_id>/', views.room_detail, name='room-detail'),
]