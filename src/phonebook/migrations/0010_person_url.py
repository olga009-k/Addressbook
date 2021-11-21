# Generated by Django 3.2.9 on 2021-11-20 05:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0009_rename_persone_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='url',
            field=models.CharField(default='https://web.telegram.org/z/', max_length=50, validators=[django.core.validators.URLValidator]),
            preserve_default=False,
        ),
    ]