# Generated by Django 3.0.2 on 2020-01-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_squashed_0006_auto_20200117_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(db_index=True, max_length=64, unique=True),
        ),
    ]
