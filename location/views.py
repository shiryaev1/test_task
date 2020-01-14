from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from location.forms import CountryCreateForm, AdministrativeRegionCreateForm, \
    MarkOfQualityCreateForm, GeographicRegionCreateForm, \
    ContainerModelCreateForm
from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, ContainerModel


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


class ContainerModelCreateView(LoginRequiredMixin, CreateView):
    model = ContainerModel
    form_class = ContainerModelCreateForm
    success_url = reverse_lazy('location:container-model-create')


def load_cities(request):
    country_id = request.GET.get('country')
    cities = GeographicRegion.objects.filter(
        country_id=country_id).order_by('name')
    geographic_region_id = request.GET.get('geographic_region')
    administrative_regions = AdministrativeRegion.objects.filter(geographic_region_id=geographic_region_id).order_by('name')
    return render(request, 'location/city_dropdown_list_options.html',
                  {
                      'cities': cities,
                      'administrative_regions': administrative_regions,
                   })

