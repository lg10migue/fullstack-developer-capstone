from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class CarMake(models.Model):
    """
    Model representing a car's make.
    """

    name = models.CharField("Car Make Name", max_length=100)
    description = models.TextField("Car Make Description")

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """
    Model representing a car's model.
    """

    CAR_TYPES = [("SEDAN", "Sedan"), ("SUV", "SUV"), ("WAGON", "Wagon")]

    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="car_models"
    )
    name = models.CharField("Car Model Name", max_length=100)
    type = models.CharField(
        "Car Model Type", max_length=10, choices=CAR_TYPES, default="SUV"
    )
    year = models.IntegerField(
        "Car Model Year",
        default=2023,
        validators=[MinValueValidator(2015), MaxValueValidator(2023)],
    )

    def __str__(self):
        return self.name
