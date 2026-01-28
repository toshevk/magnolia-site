from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.context_processors import request

# from django.urls import reverse
# from urllib.parse import urlencode
from .forms import ReservationForm, TripRequirementsForm, RoomChoiceForm, GuestDetailsForm
from .models import Room
from formtools.wizard.views import SessionWizardView

class BookingWizardView(SessionWizardView):
    form_list = [("trip_requirements", TripRequirementsForm),
                 ("room_choice", RoomChoiceForm),
                 ("guest_details", GuestDetailsForm)
    ]
    template_name = "reservations/reservation_form_wizard.html"

    def done(self, form_list, **kwargs):
        booking_requirements_form = form_list[0]
        booking_room_form = form_list[1]
        booking_details_form = form_list[2]

        print(f"{booking_details_form.cleaned_data['name']} made a new reservation!")
        print(booking_requirements_form.cleaned_data)
        print(booking_room_form.cleaned_data)
        print(booking_details_form.cleaned_data)

        return redirect("reservations:reservation_success")
        # return render(request=self.request,
        #               template_name="reservations/reservation_success.html",
        #               context={'form_list': form_list})


    def get_form_kwargs(self, step=None):
        kwargs = super().get_form_kwargs(step)

        if step == "room_choice":
            step1_data = self.get_cleaned_data_for_step("trip_requirements")

            if step1_data:
                group_size = step1_data["group_size"]
                kwargs["queryset"] = Room.objects.filter(capacity__gte=group_size)

        return kwargs

# def booking_search(request):
#     form = BookingSearchForm(request.POST or None)
#     if form.is_valid():
#         request.session["check_in"] = str(form.cleaned_data["check_in"])
#         request.session["check_out"] = str(form.cleaned_data["check_out"])
#         request.session["group_size"] = form.cleaned_data["group_size"]
#
#         return redirect("reservations:booking_result")
#
#     return render(request=request,
#                   template_name="reservations/reservation_form_step1.html",
#                   context={
#                       'form': form,
#                   })
#
# def booking_result(request):
#     check_in = request.session.get("check_in")
#     check_out = request.session.get("check_out")
#     group_size = request.session.get("group_size")
#
#     rooms = Room.objects.filter(capacity__gte=group_size)
#     return render(request=request,
#                   template_name="reservations/reservation_form_step2.html",
#                   context={
#                       'rooms': rooms,
#                   })
#
# def booking_confirm(request, pk=None):
#     room = None
#     if pk is not None:
#         room = get_object_or_404(Room, pk=pk)
#
#     room_requirements = {
#         "check_in": request.session.get("check_in"),
#         "check_out": request.session.get("check_out"),
#         "group_size": request.session.get("group_size"),
#     }
#
#     if request.method == "POST":
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             if room:
#                 reservation.room = room
#
#             form.save()
#             return redirect('reservations:reservation_success')
#
#     else:
#         if room:
#             form = ReservationForm(initial={"room": room,
#                                             "check_in": room_requirements['check_in'],
#                                             "check_out": room_requirements['check_out'],
#                                             "group_size": room_requirements['group_size']})
#         else:
#             form = ReservationForm()
#
#     return render(request=request,
#                   template_name="reservations/reservation_form_step3.html",
#                   context={
#                       'room': room,
#                       'form': form,
#                       'room_requirements': room_requirements,
#                   })

# def make_reservation(request, pk=None):
#     room = None
#     room_requirements = {
#         "check_in": request.GET.get("check_in"),
#         "check_out": request.GET.get("check_out"),
#         "group_size": request.GET.get("group_size"),
#     }
#
#     if pk is not None:
#         room = get_object_or_404(Room, pk=pk)
#
#     if request.method == "POST":
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             if room:
#                 reservation.room = room
#
#             form.save()
#             return redirect('reservations:reservation_success')
#     else:
#         if room:
#             form = ReservationForm(initial={"room": room})
#         else:
#             form = ReservationForm()
#
#     make_reservation_context = {
#         "form": form,
#         "room": room
#     }
#     return render(request=request,
#                   template_name="reservations/reservation_form.html",
#                   context=make_reservation_context)

def reservation_success(request):
    return render(request=request,
                  template_name="reservations/reservation_success.html",
                  context={})