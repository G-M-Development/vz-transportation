from django.shortcuts import render
from .models import Main


# Create your views here.

def index(request):
   main = Main.objects.all()
   return render(request, 'main/index.html', {'main': main})

def form_drivers(request):
    main = Main.objects.all()
    return render(request, 'main/form_drivers.html', {'main': main})
def form_operator(request):
    main = Main.objects.all()
    return render(request, 'main/form_operator.html', {'main': main})

def form_mechanic(request):
    main = Main.objects.all()
    return render(request, 'main/form-mechanic.html', {'main': main})