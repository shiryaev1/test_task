# Generated by Django 3.0.2 on 2020-01-14 13:57

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20200114_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
