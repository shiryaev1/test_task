from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=34)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __str__(self):
        return str(self.name)


class GeographicRegion(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('geographic region')
        verbose_name_plural = _('geographic regions')

    def __str__(self):
        return self.name


class AdministrativeRegion(models.Model):
    name = models.CharField(max_length=64)
    geographic_region = models.ForeignKey(GeographicRegion,
                                          on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('administrative region')
        verbose_name_plural = _('administrative regions')

    def __str__(self):
        return self.name


class MarkOfQuality(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    geographic_region = models.ForeignKey(GeographicRegion,
                                          on_delete=models.CASCADE)
    administrative_region = models.ForeignKey(AdministrativeRegion,
                                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('mark of quality')
        verbose_name_plural = _('mark of qualities')

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    geographic_region = models.ForeignKey(GeographicRegion,
                                          on_delete=models.CASCADE)
    administrative_region = models.ForeignKey(AdministrativeRegion,
                                              on_delete=models.CASCADE)
    mark_of_quality = models.ForeignKey(MarkOfQuality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _('packages')

    def __str__(self):
        return self.name



