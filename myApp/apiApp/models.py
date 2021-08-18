from django.db import models


# Create your models here.
class ApiApp(models.Model):
    name = models.CharField(max_length=64)
    alpha2code = models.CharField(max_length=2)
    alpha3code = models.CharField(max_length=3)
    capital = models.CharField(max_length=64)
    population = models.IntegerField()
    timezones = models.TextField(null=True)
    languages = models.TextField(null=True)
    borders = models.TextField(null=True)
