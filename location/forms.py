from django import forms
from location.models import Country, MarkOfQuality, AdministrativeRegion, \
    GeographicRegion
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
    # country = forms.ModelChoiceField(
    #     queryset=Country.objects.all())

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