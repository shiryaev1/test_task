from django import forms
from location.models import (
    Country, MarkOfQuality,
    AdministrativeRegion,
    GeographicRegion, Package
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'CREATE'))


class GeographicRegionCreateForm(forms.ModelForm):
    class Meta:
        model = GeographicRegion
        fields = (
            'name',
            'country',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'CREATE'))


class AdministrativeRegionCreateForm(forms.ModelForm):
    class Meta:
        model = AdministrativeRegion
        fields = (
            'name',
            'geographic_region',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'CREATE'))


class MarkOfQualityCreateForm(forms.ModelForm):
    class Meta:
        model = MarkOfQuality
        fields = (
            'name',
            'country',
            'geographic_region',
            'administrative_region',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'CREATE'))


class PackageCreateForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = (
            'name',
            'country',
            'geographic_region',
            'administrative_region',
            'mark_of_quality',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['geographic_region'].queryset = \
            GeographicRegion.objects.none()
        self.fields['administrative_region'].queryset = \
            AdministrativeRegion.objects.none()
        self.fields['mark_of_quality'].queryset = \
            MarkOfQuality.objects.none()
        self.set_geographic_region_queryset()
        self.set_administrative_region_queryset()
        self.set_mark_of_quality_queryset()

    def set_geographic_region_queryset(self):
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['geographic_region'].queryset = GeographicRegion.objects.filter(
                    country_id=country_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['geographic_region'].queryset = self.instance.country.geographic_regions.order_by(
                'name'
            )

    def set_administrative_region_queryset(self):
        if 'geographic_region' in self.data:
            try:
                geographic_region_id = int(self.data.get('geographic_region'))
                self.fields[
                    'administrative_region'].queryset = AdministrativeRegion.objects.filter(
                        geographic_region_id=geographic_region_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields[
                'administrative_region'].queryset = \
                self.instance.geographic_region.administrative_regions.order_by(
                    'name')

    def set_mark_of_quality_queryset(self):
        if 'administrative_region' in self.data:
            try:
                administrative_region_id = int(self.data.get(
                    'administrative_region'
                ))
                self.fields['mark_of_quality'].queryset = MarkOfQuality.objects.filter(
                        administrative_region_id=administrative_region_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields[
                'mark_of_quality'].queryset = self.instance.administrative_region.mark_of_qualities.order_by(
                    'name'
            )
