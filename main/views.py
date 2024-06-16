from django.shortcuts import render
from .models import Main

# Create your views here.

def index(request):
   main = Main.objects.all()
   
   return render(request, 'main/index.html', {'main': main})

