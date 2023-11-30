# Generated by Django 4.2.7 on 2023-11-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='visit',
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_booked',
            field=models.BooleanField(default=False, verbose_name='забронировано'),
        ),
    ]