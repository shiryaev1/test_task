from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from location.forms import CountryCreateForm, AdministrativeRegionCreateForm,\
    MarkOfQualityCreateForm, GeographicRegionCreateForm
from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality


class CountryCreateView(LoginRequiredMixin, CreateView):
    model = Country
    form_class = CountryCreateForm
    success_url = reverse_lazy('location:city-create')


class GeographicRegionCreateView(LoginRequiredMixin, CreateView):
    model = GeographicRegion
    form_class = GeographicRegionCreateForm
    success_url = reverse_lazy('location:geographic-region-create')


class AdministrativeRegionCreateView(LoginRequiredMixin, CreateView):
    model = AdministrativeRegion
    form_class = AdministrativeRegionCreateForm
    success_url = reverse_lazy('location:administrative-region-create')


class MarkOfQualityCreateView(LoginRequiredMixin, CreateView):
    model = MarkOfQuality
    form_class = MarkOfQualityCreateForm
    success_url = reverse_lazy('location:mark-quality-create')

