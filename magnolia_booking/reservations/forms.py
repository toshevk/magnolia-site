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