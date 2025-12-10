from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from urllib.parse import urlencode
from .forms import ReservationForm, BookingSearchForm
from .models import Room


def booking_search(request):
    form = BookingSearchForm(request.GET or None)
    if form.is_valid():
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']
        group_size = form.cleaned_data['group_size']

        base_url = reverse("booking_results")
        query = urlencode({
            'check_in': check_in,
            'check_out': check_out,
            'group_size': group_size,
        })
        return redirect(f"{base_url}?{query}")

    return render(request=request,
                  template_name="",
                  context={})


def make_reservation(request, pk=None):
    room = None

    if pk is not None:
        room = get_object_or_404(Room, pk=pk)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if room:
                reservation.room = room

            form.save()
            return redirect('reservations:reservation_success')
    else:
        if room:
            form = ReservationForm(initial={"room": room})
        else:
            form = ReservationForm()

    make_reservation_context = {
        "form": form,
        "room": room
    }
    return render(request=request,
                  template_name="reservations/reservation_form_step1.html",
                  context=make_reservation_context)

def reservation_success(request):
    return render(request=request,
                  template_name="reservations/reservation_success.html",
                  context={})