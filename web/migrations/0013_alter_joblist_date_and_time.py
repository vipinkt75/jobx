# Generated by Django 4.2.3 on 2023-08-18 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_joblist_date_and_time_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 5, 44, 11, 706020, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]