from django.shortcuts import render, redirect
from .forms import ReservationForm

# Create your views here.
def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    make_reservation_context = {
        "form": form
    }
    return render(request=request,
                  template_name="reservations/reservation_form.html",
                  context=make_reservation_context)