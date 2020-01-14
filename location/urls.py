from django.urls import path

from location.views import CountryCreateView, AdministrativeRegionCreateView, \
    GeographicRegionCreateView, MarkOfQualityCreateView, \
    load_cities, ContainerModelCreateView

app_name = 'location'

urlpatterns = [
    path('city/create/', CountryCreateView.as_view(), name='city-create'),
    path('administrative/region/create/',
         AdministrativeRegionCreateView.as_view(),
         name='administrative-region-create'),
    path('geographic/region/create/', GeographicRegionCreateView.as_view(),
         name='geographic-region-create'),
    path('mark/quality/create/', MarkOfQualityCreateView.as_view(),
         name='mark-quality-create'),
    path('container/model/create/', ContainerModelCreateView.as_view(),
         name='container_model_create'),
    path('container/', load_cities,
         name='ajax_load_cities'),
]

