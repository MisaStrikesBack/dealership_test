# -*- coding: utf-8 -*-
"""
vehicles views
"""
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from vehicle_inventory.models import Vehicle
from vehicle_inventory.forms import VehicleForm


class VehiclesListView(ListView):
    """
    Vehicles list view
    """
    model = Vehicle
    context_object_name = "vehicles"
    template_name = "vehicle_inventory/list.html"


class VehicleDetailView(DetailView):
    """
    Vehicle detail View
    """
    model = Vehicle
    context_object_name = "vehicle"
    template_name = "vehicle_inventory/details.html"
    delete_target = 'vehicles:delete'


class VehicleCreationView(CreateView):
    """
    Vehicle creation view
    """
    title = "Creation"
    form_class = VehicleForm
    success_url = reverse_lazy('vehicles:list')
    template_name = "vehicle_inventory/form.html"


class VehicleUpdateView(UpdateView):
    """
    Vehicle update view
    """
    title = "Update"
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle_inventory/form.html"

    def get_success_url(self):
        return reverse_lazy(
            'vehicles:details',
            kwargs={'pk': self.object.pk})


class VehicleDeleteView(DeleteView):
    """
    Vehicle delete view
    """
    model = Vehicle
    success_url = reverse_lazy('vehicles:list')
