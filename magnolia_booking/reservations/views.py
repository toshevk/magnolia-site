from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Room

# Create your views here.
def make_reservation(request, pk=None):
    room = None

    if pk is not None:
        room = get_object_or_404(Room, )

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:reservation_success')
    else:
        form = ReservationForm()

    make_reservation_context = {
        "form": form
    }
    return render(request=request,
                  template_name="reservations/reservation_form.html",
                  context=make_reservation_context)

def reservation_success(request):
    return render(request=request,
                  template_name="reservations/reservation_success.html",
                  context={})