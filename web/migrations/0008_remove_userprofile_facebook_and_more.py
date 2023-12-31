# Generated by Django 4.2.3 on 2023-08-17 10:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_userprofile_likes_alter_joblist_date_and_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joblist',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 16, 10, 19, 7, 979457, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
