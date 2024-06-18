# Generated by Django 5.0.6 on 2024-06-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerage', '0004_truckorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='bargain',
            field=models.BooleanField(default=False, verbose_name='Bargain'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='impact_protection',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Impact Protection'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='load_capacity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Load Capacity (kg)'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price ($)'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='transmission',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Transmission Type'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='year',
            field=models.DateField(blank=True, null=True, verbose_name='Year of Manufacture'),
        ),
    ]
