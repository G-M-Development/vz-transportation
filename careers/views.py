
from django.shortcuts import render
from .models import *
from main.models import Main

def careers(request):
    context = {
        "hero" : CareerHeder.objects.all(),
        "card_text" : CardText.objects.all(),
        "card_img" : CardImgFirst.objects.all(),
        "card_img_2" : CardImgSecond.objects.all(),
        "driving_history" : DrivingHistory.objects.all(),
        "we_pay" : WePay.objects.all(),
        "advantages" : AdvantagesTitle.objects.all(),
        "advantages_text" : AdvantagesText.objects.all(),
        "offers" : Offers.objects.all(),
        "offers_card" : OffersCard.objects.all(),
        "card_text_2" : CardText.objects.all(),
        "main" : Main.objects.all(),

    }




    return render(request, 'careers/careers.html', context)