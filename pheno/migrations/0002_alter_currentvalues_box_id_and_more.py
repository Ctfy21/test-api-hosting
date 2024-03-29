# Generated by Django 5.0.1 on 2024-02-02 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pheno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentvalues',
            name='box_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.box'),
        ),
        migrations.AlterField(
            model_name='currentvalues',
            name='experiment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.experiment'),
        ),
        migrations.AlterField(
            model_name='currentvalues',
            name='variety_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_values', to='pheno.variety'),
        ),
    ]
