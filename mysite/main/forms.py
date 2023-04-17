from django import forms
from .models import *

class AddPhone(forms.Form):
    phone = forms.TextInput()

