from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import TruckOrder

class TruckOrderForm(ModelForm):
    class Meta:
        model = TruckOrder
        fields = ["name", "email", "text"]
        widgets = {
            "name": TextInput(attrs={"class": "input", "placeholder": "Enter your name"}),
            "email": EmailInput(attrs={"class": "input", "placeholder": "Enter your email"}),
            "text": Textarea(attrs={
                "class": "input", 
                "placeholder": "Enter additional details or comments",
                "rows": 5,
                "cols": 30
            })
        }
