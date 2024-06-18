# Generated by Django 5.0.6 on 2024-06-18 16:41

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_main_link_first_main_link_second_main_link_third'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='main_background_img',
        ),
        migrations.AddField(
            model_name='main',
            name='main_background_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[main.models.validate_video_file_extension], verbose_name='Main Background Video'),
        ),
    ]
