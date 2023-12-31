# Generated by Django 4.2.5 on 2023-09-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('calories_per_100g', models.PositiveIntegerField(default=0, verbose_name='Calories/100g')),
                ('protein_per_100g', models.PositiveIntegerField(default=0, verbose_name='Protein/100g')),
                ('carb_per_100g', models.PositiveIntegerField(default=0, verbose_name='Carb/100g')),
                ('fats_per_100g', models.PositiveBigIntegerField(default=0, verbose_name='Fats/100g')),
            ],
            options={
                'verbose_name': 'Food Item',
                'verbose_name_plural': 'Food Items',
            },
        ),
    ]
