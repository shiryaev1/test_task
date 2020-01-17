from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from location.forms import (
    CountryCreateForm,
    AdministrativeRegionCreateForm,
    MarkOfQualityCreateForm,
    GeographicRegionCreateForm,
    PackageCreateForm
)
from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, Package


class CountryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Country
    form_class = CountryCreateForm
    success_url = reverse_lazy('location:country-create')
    success_message = 'Country was created successfully'


class GeographicRegionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GeographicRegion
    form_class = GeographicRegionCreateForm
    success_url = reverse_lazy('location:geographic-region-create')
    success_message = 'Geographic region was created successfully'


class AdministrativeRegionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AdministrativeRegion
    form_class = AdministrativeRegionCreateForm
    success_url = reverse_lazy('location:administrative-region-create')
    success_message = 'Administrative region was created successfully'


class MarkOfQualityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MarkOfQuality
    form_class = MarkOfQualityCreateForm
    success_url = reverse_lazy('location:mark-quality-create')
    success_message = 'Mark of quality was created successfully'


class PackageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Package
    form_class = PackageCreateForm
    success_url = reverse_lazy('location:package_create')
    success_message = 'Package was created successfully'


class LoadLocations(ListView):
    template_name = 'location/location_dropdown_list_options.html'

    def get_queryset(self):

        if self.request.GET.get('country'):
            country_id = self.request.GET.get('country')
            geographic_regions = GeographicRegion.objects.filter(
                country_id=country_id).order_by('name')
            return geographic_regions

        if self.request.GET.get('geographic_region'):
            geographic_region_id = self.request.GET.get('geographic_region')
            administrative_regions = AdministrativeRegion.objects.filter(
                geographic_region_id=geographic_region_id).order_by('name')
            return administrative_regions

        if self.request.GET.get('administrative_region'):
            administrative_region_id = self.request.GET.get(
                'administrative_region'
            )
            mark_of_qualities = MarkOfQuality.objects.filter(
                administrative_region_id=administrative_region_id
            ).order_by('name')
            return mark_of_qualities

    def load_geographic_regions(self):
        if self.request.GET.get('country'):
            geographic_regions = self.get_queryset()
            return geographic_regions

    def load_administrative_regions(self):
        if self.request.GET.get('geographic_region'):
            administrative_regions = self.get_queryset()
            return administrative_regions

    def load_mark_of_qualities(self):
        if self.request.GET.get('administrative_region'):
            mark_of_qualities = self.get_queryset()
            return mark_of_qualities

    def get_context_data(self, **kwargs):
        context = super(LoadLocations, self).get_context_data(**kwargs)
        context['geographic_regions'] = self.load_geographic_regions()
        context['administrative_regions'] = self.load_administrative_regions()
        context['mark_of_qualities'] = self.load_mark_of_qualities()
        return context


