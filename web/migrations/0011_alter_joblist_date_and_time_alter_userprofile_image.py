# Generated by Django 4.2.3 on 2023-08-17 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_userprofile_image_alter_joblist_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 16, 10, 45, 38, 472633, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
