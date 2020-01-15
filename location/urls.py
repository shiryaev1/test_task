from django.urls import path

from location.views import CountryCreateView, AdministrativeRegionCreateView, \
    GeographicRegionCreateView, MarkOfQualityCreateView, \
    PackageCreateView, load_locations

app_name = 'location'

urlpatterns = [
    path('country/create/', CountryCreateView.as_view(), name='country-create'),
    path('administrative/region/create/',
         AdministrativeRegionCreateView.as_view(),
         name='administrative-region-create'),
    path('geographic/region/create/', GeographicRegionCreateView.as_view(),
         name='geographic-region-create'),
    path('mark/quality/create/', MarkOfQualityCreateView.as_view(),
         name='mark-quality-create'),
    path('package/create/', PackageCreateView.as_view(),
         name='package_create'),
    path('load/location/', load_locations,
         name='ajax_load_locations'),
]

