# Generated by Django 5.0.1 on 2024-01-26 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]