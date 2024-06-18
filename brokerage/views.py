# views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Truck
from main.models import Main

class TruckDetailsView(DetailView):
    model = Truck
    template_name = 'brokerage/truck_detail.html'
    context_object_name = 'truck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = Main.objects.all()  # Додаємо додаткові дані з моделі Main
        return context

def brokerage(request):
    trucks = Truck.objects.all()
    main_items = Main.objects.all()

    context = {
        'trucks': trucks,
        'main': main_items,
    }

    return render(request, 'brokerage/brokerage.html', context)

