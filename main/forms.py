
from django.forms import ModelForm, TextInput
from .models import Driver

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ["first_name", "last_name", "phone", "date_of_birth", "work_experience"]
        widgets = {
            "first_name": TextInput(attrs={"class": "input", "placeholder": ""}),
            "last_name": TextInput(attrs={"class": "input", "placeholder": ""}),
            "phone": TextInput(attrs={"class": "input", "placeholder": ""}),
            "date_of_birth": TextInput(attrs={"class": "input", "placeholder": "", "id": "datepicker"}),
            "work_experience": TextInput(attrs={"class": "input", "placeholder": ""}),
        }




