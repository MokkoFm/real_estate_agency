# Generated by Django 2.2.4 on 2020-08-19 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_auto_20200819_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flats', to=settings.AUTH_USER_MODEL),
        ),
    ]
