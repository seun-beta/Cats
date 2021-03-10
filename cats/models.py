from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)


class Info(models.Model):
    pet_name = models.CharField(max_length=200)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    weight = models.FloatField()
