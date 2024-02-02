# Generated by Django 5.0.1 on 2024-02-02 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('max_recurrence', models.PositiveSmallIntegerField()),
                ('max_regime', models.PositiveSmallIntegerField()),
                ('max_box_variety', models.PositiveSmallIntegerField()),
                ('start_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sequence_number', models.IntegerField(null=True)),
                ('is_templated', models.BooleanField(default=False)),
                ('sequence_box_number', models.PositiveSmallIntegerField()),
                ('relative_template_percent', models.FloatField(null=True)),
                ('score', models.PositiveSmallIntegerField(null=True)),
                ('additional_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('all_plants', models.PositiveSmallIntegerField()),
                ('live_plants', models.PositiveSmallIntegerField()),
                ('grown_plants_value', models.PositiveSmallIntegerField(null=True)),
                ('live_plants_percent', models.FloatField()),
                ('box_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.box')),
                ('experiment_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.experiment')),
                ('variety_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.variety')),
            ],
        ),
    ]
