# reports/forms.py

from django import forms
from .models import Claim, Progress, Accuser, Accused

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['accuser', 'accused', 'station', 'claim_details']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['description', 'claim']
