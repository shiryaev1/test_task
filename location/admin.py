from django.contrib import admin

from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, Package

admin.site.register(Country)
admin.site.register(GeographicRegion)
admin.site.register(AdministrativeRegion)
admin.site.register(MarkOfQuality)
admin.site.register(Package)
