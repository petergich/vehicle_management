# Generated by Django 4.2 on 2023-08-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0002_aprover_journey_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='destination',
            field=models.CharField(default='Null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journey',
            name='passengers',
            field=models.CharField(default='Null', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journey',
            name='start_trip',
            field=models.CharField(default='Null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journey',
            name='stop_trip',
            field=models.CharField(default='Null', max_length=254),
            preserve_default=False,
        ),
    ]
