# Generated by Django 3.2.5 on 2021-07-19 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_temp_from_date_tem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parking_spaces',
            old_name='slot_hourly_rates',
            new_name='slot_rates',
        ),
        migrations.RemoveField(
            model_name='parking_spaces',
            name='slot_monthly_rates',
        ),
    ]
