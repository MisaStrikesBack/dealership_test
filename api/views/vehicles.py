# -*- coding: utf-8 -*-
"""
Api vehicles views
"""
from rest_framework import mixins, viewsets

from vehicle_inventory.models import Vehicle
from api.serializers import VehicleModelSerializer


class VehiclesApiListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Vehicles api list viewset
    """
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()
