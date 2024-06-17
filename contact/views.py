from django.shortcuts import render
from .models import Contact



def contact(request):
   context = {
       'contact': Contact.objects.all()
   }

   return render(request, 'contact/contact.html', context)