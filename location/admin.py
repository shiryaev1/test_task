from django.contrib import admin

from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality

admin.site.register(Country)
admin.site.register(GeographicRegion)
admin.site.register(AdministrativeRegion)
admin.site.register(MarkOfQuality)

