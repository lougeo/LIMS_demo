# Generated by Django 3.0.5 on 2020-06-04 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('date_received', models.DateField(default=django.utils.timezone.now)),
                ('date_sampled', models.DateField(default=django.utils.timezone.now)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ReportStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SieveSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('sample_day', models.DateField()),
                ('process_day', models.DateField()),
                ('wet_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dry_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('moisture_content', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mm_120', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='120 mm')),
                ('mm_80', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='80 mm')),
                ('mm_40', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='40 mm')),
                ('mm_20', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='20 mm')),
                ('mm_10', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='10 mm')),
                ('mm_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='5 mm')),
                ('mm_1', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1 mm')),
                ('mm_05', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='0.5 mm')),
                ('mm_025', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='0.25 mm')),
                ('result', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Pass'), (1, 'Warning'), (2, 'Fail')], null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sieve_samples', to='dashboard.Report')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='report_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ReportStandard'),
        ),
        migrations.AddField(
            model_name='report',
            name='technician',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Technician'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ConcreteSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('cast_date', models.DateField()),
                ('break_date', models.DateField()),
                ('days_break', models.PositiveSmallIntegerField(verbose_name='Days Untill Break')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('strength', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('result', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Pass'), (1, 'Warning'), (2, 'Fail')], null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concrete_samples', to='dashboard.Report')),
            ],
        ),
    ]
