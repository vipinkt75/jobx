# Generated by Django 4.2.3 on 2023-08-15 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_joblist_date_and_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='joblist',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 9, 40, 40, 545579, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
