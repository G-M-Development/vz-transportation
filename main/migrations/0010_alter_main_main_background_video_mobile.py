# Generated by Django 5.0.7 on 2024-07-16 11:31

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_main_main_background_video_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='main_background_video_mobile',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[main.models.validate_video_file_extension], verbose_name='Main Background Video Mobile'),
        ),
    ]
