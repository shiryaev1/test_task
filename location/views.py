from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from location.forms import (
    CountryCreateForm,
    AdministrativeRegionCreateForm,
    MarkOfQualityCreateForm,
    GeographicRegionCreateForm,
    PackageCreateForm
)
from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, Package


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryCreateForm
    success_url = reverse_lazy('location:country-create')


class GeographicRegionCreateView(CreateView):
    model = GeographicRegion
    form_class = GeographicRegionCreateForm
    success_url = reverse_lazy('location:geographic-region-create')


class AdministrativeRegionCreateView(CreateView):
    model = AdministrativeRegion
    form_class = AdministrativeRegionCreateForm
    success_url = reverse_lazy('location:administrative-region-create')


class MarkOfQualityCreateView(CreateView):
    model = MarkOfQuality
    form_class = MarkOfQualityCreateForm
    success_url = reverse_lazy('location:mark-quality-create')


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageCreateForm
    success_url = reverse_lazy('location:package_create')


def load_geographic_regions(request):
    if request.GET.get('country'):
        country_id = request.GET.get('country')
        geographic_regions = GeographicRegion.objects.filter(
            country_id=country_id).order_by('name')
        return geographic_regions


def load_administrative_regions(request):
    if request.GET.get('geographic_region'):
        geographic_region_id = request.GET.get('geographic_region')
        administrative_regions = AdministrativeRegion.objects.filter(
            geographic_region_id=geographic_region_id).order_by('name')
        return administrative_regions


def load_mark_of_qualities(request):
    if request.GET.get('administrative_region'):
        administrative_region_id = request.GET.get('administrative_region')
        mark_of_qualities = MarkOfQuality.objects.filter(
            administrative_region_id=administrative_region_id
        ).order_by('name')
        return mark_of_qualities


def load_locations(request):
    geographic_regions = load_geographic_regions(request)
    administrative_regions = load_administrative_regions(request)
    mark_of_qualities = load_mark_of_qualities(request)

    return render(request, 'location/location_dropdown_list_options.html', {
        'geographic_regions': geographic_regions,
        'administrative_regions': administrative_regions,
        'mark_of_qualities': mark_of_qualities,
    })


def landing_page(request):
    return render(request, 'landing.html')

