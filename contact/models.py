from django.db import models

# Create your models here.


class Contact(models.Model):
    main_title = models.CharField( ' Main Title ',max_length=100, default='No title')
    title = models.CharField( ' Title ',max_length=100)
    form_title = models.CharField( ' Form Title ',max_length=100, default='No title')
    phone= models.CharField(' Phone', max_length=100)
    phone_link = models.CharField( ' Phone Link ',max_length=100)
    email = models.EmailField( ' Email',max_length=100)
    email_link = models.CharField(' Email Link',max_length=100)
    location = models.CharField('Location',max_length=100)
    location_link = models.CharField('location Link',max_length=100)
    facebook= models.CharField(' Facebook',max_length=100)
    instagram = models.CharField('instagram',max_length=100)
    iframe = models.TextField( 'iframe Google Maps', null=True, blank=True)

    def __str__(self):
        return self.title