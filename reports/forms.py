from django import forms
from .models import Claim, Progress, Accuser, Accused

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['accuser', 'accused', 'station', 'claim_details', 'status']
        widgets = {
            'claim_details': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'accuser': forms.Select(attrs={'class': 'form-control'}),
            'accused': forms.Select(attrs={'class': 'form-control'}),
            'station': forms.Select(attrs={'class': 'form-control'}),
        }

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AccuserForm(forms.ModelForm):
    class Meta:
        model = Accuser
        fields = ['accuser_name', 'accuser_contact', 'accuser_location']
        widgets = {
            'accuser_name': forms.TextInput(attrs={'class': 'form-control'}),
            'accuser_contact': forms.Textarea(attrs={'class': 'form-control'}),
            'accuser_location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AccusedForm(forms.ModelForm):
    class Meta:
        model = Accused
        fields = ['accused_name', 'accused_contact', 'accused_location']
        widgets = {
            'accused_name': forms.TextInput(attrs={'class': 'form-control'}),
            'accused_contact': forms.Textarea(attrs={'class': 'form-control'}),
            'accused_location': forms.TextInput(attrs={'class': 'form-control'}),
        }
