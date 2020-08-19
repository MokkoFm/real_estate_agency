# Generated by Django 2.2.4 on 2020-08-19 15:41

from django.db import migrations
import phonenumbers


def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        flat.owner_phone_pure = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number)
    ]
