# Generated by Django 2.2.4 on 2020-08-20 15:07

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер владельца'),
        ),
    ]
