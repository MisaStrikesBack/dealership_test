# -*- coding: utf-8 -*-
"""
Vehicles forms
"""
from django import forms

from vehicle_inventory.models import Vehicle


class VehicleForm(forms.ModelForm):
    """
    Vehicles model form
    """
    class Meta:
        model = Vehicle
        fields = '__all__'
