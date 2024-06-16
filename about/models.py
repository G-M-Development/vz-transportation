import os
import hashlib
from django.db import models
from django.core.files.storage import default_storage
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class ImageModel(models.Model):
    class Meta:
        abstract = True
    
    def delete(self, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.ImageField):
                image_field = getattr(self, field.name)
                if image_field:
                    image_field.delete(save=False)
        super().delete(*args, **kwargs)


@receiver(pre_save)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        for field in instance._meta.fields:
            if isinstance(field, models.ImageField):
                old_image_field = getattr(old_instance, field.name)
                new_image_field = getattr(instance, field.name)
                if old_image_field and old_image_field != new_image_field:
                    old_image_field.delete(save=False)


def hash_file_content(file):
    hasher = hashlib.sha256()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()

def unique_file_name(instance, filename, field_name):
    ext = filename.split('.')[-1]
    hash_name = hash_file_content(getattr(instance, field_name))
    filename = f"{hash_name}.{ext}"
    file_path = os.path.join('images/', filename)
    if default_storage.exists(file_path):
        return file_path
    return file_path
class AboutHero(ImageModel):
#  hero
    main_title = models.CharField( 'Main Title',max_length=100 , default='No title')
    main_text= models.TextField('Main Text', null=True, blank=True)
    main_background_img = models.ImageField('Main Image', upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.main_title
    
class  HeroCard(ImageModel):
    card_text= models.TextField('Card Text', null=True, blank=True)
    card_img = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)
    card_description = models.CharField('Card Description', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.card_text
    
# teem
class AboutTeem(ImageModel):
    teem_title= models.CharField( 'Teem Title',max_length=100 , default='No title')
    
    def __str__(self):
        return self.teem_title
    
class AboutCardTeem(ImageModel):
    card_name = models.CharField('Card Name', max_length=100, default='No title')
    card_position = models.CharField('Card Position', max_length=100, default='No title')
    card_img = models.ImageField('Card Image', upload_to='images/', null=True, blank=True)
    card_description = models.TextField('Card Description', null=True, blank=True)

    def __str__(self):
        return self.card_name

    # video
class AboutCompany(models.Model):
    Company_title= models.CharField( 'Kompany Title',max_length=100 , default='No title')
    iframe = models.TextField('Iframe Youtube Video', null=True, blank=True)

    def __str__(self):
        return self.Company_title
    
# maps

class CardMap(models.Model):
    card_title= models.CharField( 'Card Title',max_length=100 , default='No title')
    card_text = models.TextField('Card Text', null=True, blank=True)
    card_iframe = models.TextField('Card Iframe Google Maps', null=True, blank=True)

    def __str__(self):
        return self.card_title
    

# info

class AboutInfo(models.Model):
    info_title= models.CharField( 'Info Title',max_length=100 , default='No title')
    info_background_img = models.ImageField('Info Background Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.info_title