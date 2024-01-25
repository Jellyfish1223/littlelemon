from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255)
    guests = models.PositiveSmallIntegerField(validators=[MaxValueValidator(6)])
    date = models.DateTimeField()

class Menu(models.Model):
    id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5)])

    