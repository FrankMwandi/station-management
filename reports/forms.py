from django import forms
from .models import Claim, Progress

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['accuser', 'accused', 'station', 'claim_details', 'status']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['description']