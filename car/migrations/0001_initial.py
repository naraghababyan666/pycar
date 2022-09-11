# Generated by Django 4.1.1 on 2022-09-09 12:38

import car.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('engine_type', models.CharField(max_length=255)),
                ('odometer', models.IntegerField(default=0)),
                ('primary_damage', models.CharField(max_length=255)),
                ('secondary_damage', models.CharField(blank=True, max_length=255, null=True)),
                ('highlights', models.CharField(max_length=255)),
                ('estimated_value', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('sale_date', models.CharField(max_length=255)),
                ('photo_exterior_1', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_exterior_2', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_exterior_3', models.ImageField(blank=True, null=True, upload_to=car.models.img_path)),
                ('photo_exterior_4', models.ImageField(blank=True, null=True, upload_to=car.models.img_path)),
                ('photo_interior_1', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_interior_2', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_interior_3', models.ImageField(blank=True, null=True, upload_to=car.models.img_path)),
                ('photo_interior_4', models.ImageField(blank=True, null=True, upload_to=car.models.img_path)),
                ('photo_engine', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_speedometer', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('photo_vin', models.ImageField(blank=True, upload_to=car.models.img_path)),
                ('vin', models.CharField(max_length=255)),
                ('lot', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]