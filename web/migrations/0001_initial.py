# Generated by Django 4.2.3 on 2023-08-11 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applyform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jobList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('jobtype', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime(2023, 9, 10, 11, 22, 43, 223696, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)')),
                ('Job_description', models.TextField(blank=True, null=True)),
                ('Responsibility', models.TextField(blank=True, null=True)),
                ('Vacancy', models.IntegerField()),
                ('company_detail', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('sender_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]