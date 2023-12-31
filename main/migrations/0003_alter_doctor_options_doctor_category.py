# Generated by Django 4.2.7 on 2023-11-23 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_doctor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ('specialization',), 'verbose_name': 'Доктор', 'verbose_name_plural': 'Доктора'},
        ),
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.testcategory', verbose_name='категория'),
        ),
    ]
