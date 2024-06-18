# services/views.py
from django.shortcuts import render
from .models import *
from main.models import Main

def services(request):
    context = {
      "services" : Services.objects.all(),
      'text': TextServices.objects.all(),
      'main': Main.objects.all()
    }
    return render(request, 'services/services.html', context)






