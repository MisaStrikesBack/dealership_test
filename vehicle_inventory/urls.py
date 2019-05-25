# -*- coding: utf-8 -*-
"""
vehicle_inventory urls
"""
from django.urls import path, include

from vehicle_inventory.views import (
    VehiclesListView, VehicleDetailView, VehicleDeleteView,
    VehicleCreationView, VehicleUpdateView, LandingView)

app_name = "vehicle_inventory"

vehicles_patterns = ([
    path('list/', VehiclesListView.as_view(), name='list'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='details'),
    path('create/', VehicleCreationView.as_view(), name='create'),
    path('update/<int:pk>/', VehicleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', VehicleDeleteView.as_view(), name='delete'),
])

urlpatterns = [
    path('vehicles/', include(vehicles_patterns)),
    path('', LandingView.as_view(), name="landing"),
]
