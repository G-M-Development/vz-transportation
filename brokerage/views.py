from django.shortcuts import render
from .models import Truck
from django.views.generic import DeleteView


class TruckDetailsView(DeleteView):
    model = Truck
    template_name = 'brokerage/truck_detail.html'
    context_object_name = 'truck'

def brokerage(request):
    trucks = Truck.objects.all()

    context = {
        'trucks': trucks,
      
    }

    return render(request, 'brokerage/brokerage.html',  context)
