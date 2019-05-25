# -*- coding: utf-8 -*-
"""
Vehicles models
"""
from django.db import models
from django.core.validators import MinValueValidator


class Vehicle(models.Model):
    """
    Vehicle information
    """
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1), ])
    description = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50)
    doors = models.PositiveIntegerField(validators=[MinValueValidator(2), ])
    lot = models.CharField(max_length=50)

    def __str__(self):
        return "{0} {1} {2}".format(
            self.make, self.model, self.year)
