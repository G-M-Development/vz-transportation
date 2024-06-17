# services/views.py
from django.shortcuts import render
from .models import *

def services(request):
    context = {
      "services" : Services.objects.all(),
      'text': TextServices.objects.all()
    }
    return render(request, 'services/services.html', context)






