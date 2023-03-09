# Generated by Django 3.2 on 2023-03-04 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1)], verbose_name='Дата выхода'),
        ),
    ]
