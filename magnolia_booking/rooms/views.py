from django.shortcuts import render, get_object_or_404
from .models import Room

# Create your views here.
def room_list(request):
    room_list = Room.objects.all()
    room_list_context = {
        'room_list': room_list
    }
    return render(request=request,
                  template_name="rooms/room-list.html",
                  context=room_list_context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    amenities = room.amenities.split(',') if room.amenities else []
    room_detail_context = {
        'room': room,
        'amenities': amenities,
    }
    return render(request=request,
                  template_name="rooms/room-detail.html",
                  context=room_detail_context)