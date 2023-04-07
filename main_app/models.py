from django.db import models

# Create your models here.

class Snowboard(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Snowboarding(models.Model):
    name = models.CharField(max_length=100)

class Snowboarder(models.Model):
    name = models.CharField(max_length=100)
    snowboarding = models.ForeignKey(Snowboarding, on_delete=models.CASCADE, related_name='snowboarders')