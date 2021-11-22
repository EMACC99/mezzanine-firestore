from django.core import validators
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator


class Paciente(models.Model):
    GENERO_CHOICES = (
        ('1', 'Masculino'),
        ('2', 'Femenino'),
        ('3', 'Otro')
    )

    first_name = models.CharField(max_length=128)

    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=16, choices = GENERO_CHOICES)
    genero_otro = models.CharField(max_length=32, blank=True, null = True)
    fecha_nacimiento = models.DateField()
    country = CountryField()
    weight = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)], default=0) #kg
    heigth = models.FloatField(validators=[MinValueValidator(0.), MaxValueValidator(2.5)], default=0) #m