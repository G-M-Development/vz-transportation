from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField( 'Main Title', max_length=100, default='No title')
    img = models.ImageField(' Main Image', upload_to='images/', null=True, blank=True)
    sub_title = models.TextField('Main  Text ', null=True, blank=True)


    def __str__(self):
        return self.title
    
class TextServices(models.Model):
    text = models.TextField('Main  Text ', null=True, blank=True)

    def __str__(self):
        return self.text