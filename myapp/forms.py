# forms.py

from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'  # Or specify the fields you want to include in the form
