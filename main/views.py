from django.shortcuts import render, redirect
from .models import Main
from .forms import DriverForm

# Create your views here.

def index(request):
   main = Main.objects.all()
   return render(request, 'main/index.html', {'main': main})

def form_drivers(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form = DriverForm()
    return render(request, 'main/form_drivers.html', {'form': form})
def form_operator(request):
    return render(request, 'main/form_operator.html')

def form_mechanic(request):
    return render(request, 'main/form-mechanic.html')