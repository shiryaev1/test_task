# Generated by Django 3.0.2 on 2020-01-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20200117_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativeregion',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='geographicregion',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
