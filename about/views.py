from django.shortcuts import render
from .models import *
from main.models import Main

def about(request):

    context = {
        'about_hero': AboutHero.objects.all(),
        'about_company': AboutCompany.objects.all(),
        'about_info': AboutInfo.objects.all(),
        'about_teem': AboutTeem.objects.all(),
        'card_map': CardMap.objects.all(),
        'hero_card': HeroCard.objects.all(),
        'about_card_teem':AboutCardTeem.objects.all(),
        'main': Main.objects.all(),
    }
    
    return render(request, 'about/about.html', context)
