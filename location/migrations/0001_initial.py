# Generated by Django 3.0.2 on 2020-01-14 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'administrative region',
                'verbose_name_plural': 'administrative regions',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=34)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='GeographicRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
            ],
            options={
                'verbose_name': 'geographic region',
                'verbose_name_plural': 'geographic regions',
            },
        ),
        migrations.CreateModel(
            name='MarkOfQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('administrative_region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.AdministrativeRegion')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
                ('geographic_region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.GeographicRegion')),
            ],
            options={
                'verbose_name': 'mark of quality',
                'verbose_name_plural': 'mark of qualities',
            },
        ),
        migrations.CreateModel(
            name='ContainerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('administrative_region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.AdministrativeRegion')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
                ('geographic_region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.GeographicRegion')),
                ('mark_of_quality', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.MarkOfQuality')),
            ],
            options={
                'verbose_name': 'container',
                'verbose_name_plural': 'containers',
            },
        ),
        migrations.AddField(
            model_name='administrativeregion',
            name='geographic_region',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.GeographicRegion'),
        ),
    ]
