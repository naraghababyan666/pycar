import datetime
import time

from django.db import models


def img_path(instance, filename):
    return f"{instance.make}-{instance.lot}/{filename} "


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    engine_type = models.CharField(max_length=255)
    odometer = models.IntegerField(default=0)
    primary_damage = models.CharField(max_length=255)
    secondary_damage = models.CharField(max_length=255, null=True, blank=True)
    highlights = models.CharField(max_length=255)
    estimated_value = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255)
    sale_date = models.CharField(max_length=255)
    photo_exterior_1 = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_exterior_2 = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_exterior_3 = models.ImageField(upload_to=img_path, null=True, blank=True)
    photo_exterior_4 = models.ImageField(upload_to=img_path, null=True, blank=True)
    photo_interior_1 = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_interior_2 = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_interior_3 = models.ImageField(upload_to=img_path, null=True, blank=True)
    photo_interior_4 = models.ImageField(upload_to=img_path, null=True, blank=True)
    photo_engine = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_speedometer = models.ImageField(upload_to=img_path, null=False, blank=True)
    photo_vin = models.ImageField(upload_to=img_path, null=False, blank=True)
    vin = models.CharField(max_length=255)
    lot = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.make
