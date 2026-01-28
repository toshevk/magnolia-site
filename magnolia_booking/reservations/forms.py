import datetime
from django import forms
from .models import Reservation, Room

class ReservationForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Reservation
        fields = ['room',
                  'check_in',
                  'check_out',
                  'group_size',
                  'guest_name',
                  'guest_telephone',
                  'guest_email'
        ]

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise forms.ValidationError("Bot detected.")
        return self.cleaned_data['honeypot']

class TripRequirementsForm(forms.Form):
    check_in = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    group_size = forms.IntegerField(min_value=1, max_value=10)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("check_in") and cleaned.get("check_out"):
            if cleaned["check_in"] < datetime.date.today():
                raise forms.ValidationError("Earliest you can check-in is today.")
            if cleaned["check_out"] <= cleaned["check_in"]:
                raise forms.ValidationError("Check-out must be after check-in.")
        return cleaned

class RoomChoiceForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.none(),
                                  empty_label='Select a Room')

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop("queryset", Room.objects.none())
        super().__init__(*args, **kwargs)
        self.fields["room"].queryset = queryset

class GuestDetailsForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField()
