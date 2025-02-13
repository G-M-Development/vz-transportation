# Generated by Django 5.0.6 on 2024-06-18 17:13

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_main_main_background_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='main_background_video_mobile',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[main.models.validate_video_file_extension], verbose_name='Main Background Video'),
        ),
    ]
