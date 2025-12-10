from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Reservation
        fields = ['room', 'guest_name', 'check_in', 'check_out', 'group_size']
        widgets = {
            'check_in': forms.DateInput(attrs={'type':'date'}),
            'check_out': forms.DateInput(attrs={'type':'date'})
        }

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise forms.ValidationError("Bot detected.")
        return self.cleaned_data['honeypot']

class BookingSearchForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label='Check-in')

    check_out = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label="Check-out")

    group_size = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Number of Guests")

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise forms.ValidationError("Bot detected.")
        return self.cleaned_data['honeypot']