# Generated by Django 2.1 on 2018-08-15 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
