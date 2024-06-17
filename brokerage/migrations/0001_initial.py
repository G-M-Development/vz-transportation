# Generated by Django 5.0.6 on 2024-06-17 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Truck Name')),
                ('year', models.PositiveIntegerField(verbose_name='Year of Manufacture')),
                ('load_capacity', models.PositiveIntegerField(verbose_name='Load Capacity (kg)')),
                ('speed', models.PositiveIntegerField(verbose_name='Speed (km/h)')),
                ('transmission', models.CharField(max_length=100, verbose_name='Transmission Type')),
                ('impact_protection', models.CharField(max_length=100, verbose_name='Impact Protection')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price ($)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='trucks/', verbose_name='Main Image')),
                ('text', models.TextField(verbose_name='Comment Text')),
            ],
        ),
        migrations.CreateModel(
            name='TruckImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='truck_images/', verbose_name='Image')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='brokerage.truck')),
            ],
        ),
    ]
