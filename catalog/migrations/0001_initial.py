# Generated by Django 5.1.4 on 2025-01-08 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=35)),
                ('patronymic_name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=2)),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.employee')),
            ],
        ),
    ]
