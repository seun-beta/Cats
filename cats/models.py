from django.db import models
from django.core.validators import MinLengthValidator


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Enter the breed of cat',
        validators=[MinLengthValidator(2, """
        Breed name must have more than 2 characters
        """)]
    )

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text='Enter the name of your pet',
        validators=[MinLengthValidator(1, """
        Pet name must have 1 or more characters
        """)]
    )
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    weight = models.FloatField()
    foods = models.CharField(max_length=300)

    def __str__(self):
        return self.pet_name
