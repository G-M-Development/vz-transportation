# Generated by Django 5.0.6 on 2024-06-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_title', models.CharField(default='No title', max_length=100, verbose_name='Kompany Title')),
                ('iframe', models.TextField(blank=True, null=True, verbose_name='Iframe Youtube Video')),
            ],
        ),
        migrations.CreateModel(
            name='AboutHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(default='No title', max_length=100, verbose_name='Main Title')),
                ('main_text', models.TextField(blank=True, null=True, verbose_name='Main Text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_title', models.CharField(default='No title', max_length=100, verbose_name='Info Title')),
                ('info_background_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Info Background Image')),
            ],
        ),
        migrations.CreateModel(
            name='AboutTeem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teem_title', models.CharField(default='No title', max_length=100, verbose_name='Teem Title')),
                ('card_name', models.CharField(default='No title', max_length=100, verbose_name='Card Name')),
                ('card_position', models.CharField(default='No title', max_length=100, verbose_name='Card Position')),
                ('card_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Card Image')),
                ('card_description', models.TextField(blank=True, null=True, verbose_name='Card Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(default='No title', max_length=100, verbose_name='Card Title')),
                ('card_text', models.TextField(blank=True, null=True, verbose_name='Card Text')),
                ('card_iframe', models.TextField(blank=True, null=True, verbose_name='Card Iframe Google Maps')),
            ],
        ),
        migrations.CreateModel(
            name='HeroCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_text', models.TextField(blank=True, null=True, verbose_name='Card Text')),
                ('card_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Card Image')),
                ('card_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Card Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
