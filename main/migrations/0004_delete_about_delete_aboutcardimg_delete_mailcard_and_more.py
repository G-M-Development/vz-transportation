# Generated by Django 5.0.6 on 2024-06-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutcardimg_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='AboutCardImg',
        ),
        migrations.DeleteModel(
            name='MailCard',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceItem',
        ),
        migrations.RemoveField(
            model_name='main',
            name='mail_background_img',
        ),
        migrations.AddField(
            model_name='main',
            name='about_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='About Image'),
        ),
        migrations.AddField(
            model_name='main',
            name='about_sub_title',
            field=models.CharField(default='No title', max_length=100, verbose_name=' About Sub Title'),
        ),
        migrations.AddField(
            model_name='main',
            name='about_text',
            field=models.TextField(default='No text', verbose_name='About Text'),
        ),
        migrations.AddField(
            model_name='main',
            name='about_title',
            field=models.CharField(default='No title', max_length=100, verbose_name='About Title'),
        ),
        migrations.AddField(
            model_name='main',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='main',
            name='main_background_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Main Background Image'),
        ),
        migrations.AddField(
            model_name='main',
            name='main_card_text',
            field=models.TextField(blank=True, null=True, verbose_name='Main Card Text'),
        ),
        migrations.AddField(
            model_name='main',
            name='main_card_title',
            field=models.CharField(default='No title', max_length=100, verbose_name='Main Card Title'),
        ),
        migrations.AddField(
            model_name='main',
            name='service_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Service Image'),
        ),
        migrations.AddField(
            model_name='main',
            name='service_text',
            field=models.TextField(default='No text', verbose_name='Service Text'),
        ),
        migrations.AddField(
            model_name='main',
            name='service_title',
            field=models.CharField(default='No title', max_length=100, verbose_name='Service Title'),
        ),
        migrations.AlterField(
            model_name='main',
            name='main_title',
            field=models.CharField(default='No title', max_length=100, verbose_name='Main Title'),
        ),
    ]
