from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from location.forms import CountryCreateForm, AdministrativeRegionCreateForm, \
    MarkOfQualityCreateForm, GeographicRegionCreateForm, \
    PackageCreateForm
from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, Package


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


class PackageCreateView(LoginRequiredMixin, CreateView):
    model = Package
    form_class = PackageCreateForm
    success_url = reverse_lazy('location:container_model_create')


def load_locations(request):
    country_id = request.GET.get('country')
    geographic_regions = GeographicRegion.objects.filter(
        country_id=country_id).order_by('name')
    geographic_region_id = request.GET.get('geographic_region')
    administrative_regions = AdministrativeRegion.objects.filter(
        geographic_region_id=geographic_region_id).order_by('name')
    administrative_region_id = request.GET.get('administrative_region')
    mark_of_qualities = MarkOfQuality.objects.filter(
        administrative_region_id=administrative_region_id).order_by('name')
    return render(request, 'location/location_dropdown_list_options.html',
                  {
                      'geographic_regions': geographic_regions,
                      'administrative_regions': administrative_regions,
                      'mark_of_qualities': mark_of_qualities,
                   })

