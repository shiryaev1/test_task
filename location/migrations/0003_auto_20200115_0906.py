# Generated by Django 3.0.2 on 2020-01-15 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200115_0658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': 'package', 'verbose_name_plural': 'packages'},
        ),
    ]
