import os
import hashlib
from django.db import models
from django.core.files.storage import default_storage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
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
    try:
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            for field in instance._meta.fields:
                if isinstance(field, models.ImageField):
                    old_image_field = getattr(old_instance, field.name)
                    new_image_field = getattr(instance, field.name)
                    if old_image_field and old_image_field != new_image_field:
                        old_image_field.delete(save=False)
    except ObjectDoesNotExist:
        pass  # Handle the case where the instance does not exist anymore

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


def validate_video_file_extension(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError(u'Only .mp4 files are allowed.')


class Main(ImageModel):
    # Header nav menu
    Link_first = models.CharField('Link First', max_length=100, default='No title')
    Link_second = models.CharField('Link Second', max_length=100, default='No title')
    Link_third = models.CharField('Link Third', max_length=100, default='No title')
    # Main 
    main_title = models.CharField('Main Title', max_length=100, default='No title')
    main_background_video = models.FileField(
        'Main Background Video', 
        upload_to='videos/', 
        null=True, 
        blank=True, 
        validators=[validate_video_file_extension]
    )
    main_background_video_mobile = models.FileField(
        'Main Background Video Mobile', 
        upload_to='videos/', 
        null=True, 
        blank=True, 
        validators=[validate_video_file_extension]
    )
    # Main Card
    main_card_title_first = models.CharField('Main Card Title First', max_length=100, default='No title')
    main_card_text_first = models.TextField('Main Card Text First', null=True, blank=True)
    main_card_title_second = models.CharField('Main Card Title Second', max_length=100, default='No title')
    main_card_text_second = models.TextField('Main Card Text Second', null=True, blank=True)
    main_card_title_three = models.CharField('Main Card Title Third', max_length=100, default='No title')
    main_card_text_three = models.TextField('Main Card Text Third', null=True, blank=True)
    # service card
    service_sub_title = models.CharField('Service Sub Title', max_length=100, default='No title') 
    service_title = models.CharField('Service Title', max_length=100, default='No title')
    service_title_first = models.CharField('Service Title First', max_length=100, default='No title')
    service_text_first = models.TextField('Service Text First', default='No text')
    service_img_first = models.ImageField('Service Image First', upload_to='images/', null=True, blank=True)
    service_description_first = models.CharField('Service Description First', max_length=255, null=True, blank=True)
    service_title_second = models.CharField('Service Title Second', max_length=100, default='No title')
    service_text_second = models.TextField('Service Text Second', default='No text')
    service_img_second = models.ImageField('Service Image Second', upload_to='images/', null=True, blank=True)
    service_description_second = models.CharField('Service Description Second', max_length=255, null=True, blank=True)
    service_title_three = models.CharField('Service Title Third', max_length=100, default='No title')
    service_text_three = models.TextField('Service Text Third', default='No text')
    service_img_three = models.ImageField('Service Image Third', upload_to='images/', null=True, blank=True)
    service_description_three = models.CharField('Service Description Third', max_length=255, null=True, blank=True)
    service_title_fourth = models.CharField('Service Title Fourth', max_length=100, default='No title')
    service_text_fourth = models.TextField('Service Text Fourth', default='No text')
    service_img_fourth = models.ImageField('Service Image Fourth', upload_to='images/', null=True, blank=True)
    service_description_fourth = models.CharField('Service Description Fourth', max_length=255, null=True, blank=True)
    # About card
    about_sub_title = models.CharField(' About Sub Title', max_length=100, default='No title')
    about_title = models.CharField('About Title', max_length=100, default='No title')
    about_text = models.TextField('About Text', default='No text')
    about_img_first = models.ImageField('About Image', upload_to='images/', null=True, blank=True)
    about_description_first = models.CharField(' About Description First', max_length=255, null=True, blank=True)
    about_img_second = models.ImageField('About Image', upload_to='images/', null=True, blank=True)
    about_description_second = models.CharField(' About Description Second', max_length=255, null=True, blank=True)
    about_img_third = models.ImageField('About Image', upload_to='images/', null=True, blank=True)
    about_description_third = models.CharField(' About Description Third', max_length=255, null=True, blank=True)
    about_img_fourth = models.ImageField('About Image', upload_to='images/', null=True, blank=True)
    about_description_fourth = models.CharField(' About Description Fourth', max_length=255, null=True, blank=True)
    # Careers
    careers_sub_title = models.CharField(' Careers Sub Title', max_length=100, default='No title')
    careers_title = models.CharField(' Careers Title', max_length=100, default='No title')
    careers_text = models.TextField(' Careers Text', default='No text')
    careers_background_img = models.ImageField(' Careers Image', upload_to='images/', null=True, blank=True)
    careers_card_img_first = models.ImageField(' Careers Card Image First', upload_to='images/', null=True, blank=True)
    careers_description_first = models.CharField(' Careers Description First', max_length=255, null=True, blank=True)
    careers_card_img_second = models.ImageField(' Careers Card Image Second', upload_to='images/', null=True, blank=True)
    careers_description_second = models.CharField(' Careers Description Second', max_length=255, null=True, blank=True)
    careers_card_img_third = models.ImageField(' Careers Card Image Third', upload_to='images/', null=True, blank=True)
    careers_description_third = models.CharField(' Careers Description Third', max_length=255, null=True, blank=True)
    # DEVELOPMENT
    development_sub_title = models.CharField(' Development Sub Title', max_length=100, default='No title')
    development_title = models.CharField(' Development Title', max_length=100, default='No title')
    development_text = models.TextField(' Development Text', default='No text')
    development_background_img = models.ImageField(' Development Image', upload_to='images/', null=True, blank=True)
    # PROJECTS
    projects_main_title = models.CharField(' Projects Main Title', max_length=100, default='No title')
    projects_card_title_first = models.CharField(' Projects Card Title First', max_length=100, default='No title')
    projects_card_background_img_first = models.ImageField(' Projects Card Image', upload_to='images/', null=True, blank=True)
    projects_card_title_second = models.CharField(' Projects Card Title Second', max_length=100, default='No title')
    projects_card_background_img_second = models.ImageField(' Projects Card Image', upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.main_title



class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    work_experience = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"