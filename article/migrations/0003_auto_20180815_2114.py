# Generated by Django 2.1 on 2018-08-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
