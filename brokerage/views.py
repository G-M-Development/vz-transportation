from django.shortcuts import render
from .models import Truck
from .forms import TruckOrderForm
from django.views.generic import DeleteView

# Create your views here.

class TruckDetailsView(DeleteView):
    model = Truck
    template_name = 'brokerage/truck_detail.html'
    context_object_name = 'truck'




def brokerage(request):
    trucks = Truck.objects.all()
    form = TruckOrderForm()  
    context = {
        'trucks': trucks,
        'form': form
    }

    return render(request, 'brokerage/brokerage.html',  context)
