from django.shortcuts import render
from .models import Contact
from main.models import Main



def contact(request):
   context = {
       'contact': Contact.objects.all(),
       'main': Main.objects.all()
   }

   return render(request, 'contact/contact.html', context)