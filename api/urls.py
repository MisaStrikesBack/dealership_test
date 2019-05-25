# -*- coding: utf-8 -*-
"""
api urls
"""
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.views import VehiclesApiListView

app_name = "vehicle_inventory"

vehicles_router = SimpleRouter()

# contact services
vehicles_router.register(
    r'vehicles', VehiclesApiListView, base_name='api_vehicles')

urlpatterns = [
    path('portal/', include(vehicles_router.urls)),
]
