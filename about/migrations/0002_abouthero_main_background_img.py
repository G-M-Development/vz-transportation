# Generated by Django 5.0.6 on 2024-06-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouthero',
            name='main_background_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Main Image'),
        ),
    ]
