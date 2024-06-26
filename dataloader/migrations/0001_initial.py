# Generated by Django 5.0.3 on 2024-03-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, verbose_name='event_name')),
                ('city_name', models.CharField(max_length=255, verbose_name='city_name')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('time', models.TimeField(auto_now=True, verbose_name='time')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
            ],
        ),
    ]
