# Generated by Django 3.0.5 on 2020-05-30 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20200530_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concretesample',
            name='break_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='concretesample',
            name='cast_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
