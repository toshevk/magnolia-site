from django.shortcuts import render
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