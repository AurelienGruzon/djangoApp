from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length = 100)
    genre = models.fields.CharField(choices = Genre.choices, max_length = 5)
    biography = models.fields.CharField(max_length = 100)
    year_formed = models.fields.IntegerField(validators = [MinValueValidator(1900), MaxValueValidator(2023)])
    active = models.fields.BooleanField(default = True)
    official_homepage = models.fields.URLField(null = True, blank = True)
    
class Listing(models.Model):

    def __str__(self):
        return f'{self.title}'
    
    class Type(models.TextChoices):
        RECORD = "RD"
        CLOTHING = "CL"
        POSTERS = "PT"
        MISCELLANEOUS = "MS"

    title = models.fields.CharField(default = "", max_length = 100)
    description = models.fields.CharField(default = "", max_length = 500)
    sold = models.fields.BooleanField(default = False)
    year = models.fields.IntegerField(default = 2000, validators = [MinValueValidator(1900), MaxValueValidator(2024)])
    ltype = models.fields.CharField(default = "RD", choices = Type.choices, max_length = 5)
    band = models.ForeignKey(Band, null = True, on_delete = models.SET_NULL)
