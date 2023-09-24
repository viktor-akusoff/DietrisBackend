# Generated by Django 4.2.5 on 2023-09-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='fats_per_100g',
            field=models.PositiveIntegerField(default=0, verbose_name='Fats/100g'),
        ),
    ]