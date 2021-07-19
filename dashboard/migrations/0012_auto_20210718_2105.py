# Generated by Django 3.2.5 on 2021-07-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210718_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot_duration_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.TextField(blank=True, max_length='100')),
                ('to_date', models.TextField(blank=True, max_length='100')),
            ],
        ),
        migrations.RemoveField(
            model_name='temp',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='temp',
            name='to_data',
        ),
        migrations.AlterField(
            model_name='slots_booking_table',
            name='Slot_duration',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.slot_duration_table'),
        ),
    ]
