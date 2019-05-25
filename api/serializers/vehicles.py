# -*- coding: utf-8 -*-
"""
vehicles serializers
"""
from rest_framework import serializers

from vehicle_inventory.models import Vehicle


class VehicleModelSerializer(serializers.ModelSerializer):
    """
    Vehicles model serializer
    """
    class Meta:
        model = Vehicle
        fields = '__all__'
