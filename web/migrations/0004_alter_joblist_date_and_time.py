# Generated by Django 4.2.3 on 2023-08-11 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_joblist_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 12, 12, 39, 806761, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
