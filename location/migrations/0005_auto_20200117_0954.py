# Generated by Django 3.0.2 on 2020-01-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20200116_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
