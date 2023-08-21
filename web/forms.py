from django import forms
from .models import applyform
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ApplyForm(forms.ModelForm):
    class Meta:
        model = applyform
        fields = ['job','email', 'name', 'email', 'website', 'file']
        widgets = {
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Job', 'readonly': 'readonly'}),
            'sender_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Job', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portfolio Website'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control bg-white'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'