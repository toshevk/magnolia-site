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
                  template_name="reservations/reservation_form_step1.html",
                  context={
                      'form': form,
                  })

def booking_result(request):
    room_requirements = {
        "check_in": request.GET.get("check_in"),
        "check_out": request.GET.get("check_out"),
        "group_size": request.GET.get("group_size"),
    }

    rooms = Room.objects.filter(capacity__gte=room_requirements['group_size'])
    return render(request=request,
                  template_name="reservations/reservation_form_step2.html",
                  context={
                      'room_requirements': room_requirements,
                      'rooms': rooms,
                  })

def booking_confirm(request, pk=None):
    room = None
    room_requirements = {
        "check_in": request.GET.get("check_in"),
        "check_out": request.GET.get("check_out"),
        "group_size": request.GET.get("group_size"),
    }

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

    #
    #   OTKRIJ JA GRESKATA
    #   VIDI STO PUSTA POST REQUESTOT DO MODEL FORM
    #
    #   MOZNO E INITIAL VREDNOSTITE
    #

    else:
        if room:
            form = ReservationForm(initial={"room": room,
                                            "check_in": room_requirements['check_in'],
                                            "check_out": room_requirements['check_out'],
                                            "group_size": room_requirements['group_size']})
        else:
            form = ReservationForm()

    return render(request=request,
                  template_name="reservations:reservation_step3.html",
                  context={
                      'room': room,
                      'form': form,
                      'room_requirements': room_requirements,
                  })

def make_reservation(request, pk=None):
    room = None
    room_requirements = {
        "check_in": request.GET.get("check_in"),
        "check_out": request.GET.get("check_out"),
        "group_size": request.GET.get("group_size"),
    }

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
                  template_name="reservations/reservation_form.html",
                  context=make_reservation_context)

def reservation_success(request):
    return render(request=request,
                  template_name="reservations/reservation_success.html",
                  context={})