from django.db import models

# Create your models here.


class CareerHeder(models.Model):
    title = models.CharField(' Title Hero',max_length=100)
    img = models.ImageField('Hero Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class CardText(models.Model):
    card_title = models.CharField('Card Title',max_length=100)
    card_description_first = models.TextField('Card Description')
    card_description_second = models.TextField('Card Description')

    def __str__(self):
        return self.card_title
    

class CardImgFirst(models.Model):
    img = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.img)
    
class AdvantagesTitle(models.Model):
    title = models.CharField('Title',max_length=100)

    def __str__(self):
        return self.title

class AdvantagesText(models.Model):
    text = models.TextField('Text')

    def __str__(self):
        return str(self.text)


class CardImgSecond(models.Model):
    img = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.img)
    

class DrivingHistory(models.Model):
    title = models.CharField('Title',max_length=100)
    text= models.TextField('Text')
    img_background = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
class Offers(models.Model):
    title = models.CharField('Title',max_length=100)

    def __str__(self):
        return str(self.title)
    
class OffersCard(models.Model):
    text= models.TextField('Text')
    img_background = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.text)


class WePay(models.Model):
    title = models.CharField('Title',max_length=100)
    text= models.TextField('Text')
    sub_title = models.CharField('Sub Title',max_length=100)
    img_background = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)


    def __str__(self):
        return str(self.title)
  