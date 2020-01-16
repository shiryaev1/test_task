from django.test import TestCase, Client

from location.models import Country, GeographicRegion, AdministrativeRegion, \
    MarkOfQuality, Package


def create_country():
    country = Country.objects.create(name='TestCountry')
    return country


def create_geographic_region():
    geographic_region = GeographicRegion.objects.create(
        name='TestGeographicRegion',
        country=create_country()
    )
    return geographic_region


def create_administrative_region():
    administrative_region = AdministrativeRegion.objects.create(
        name='TestAdministrativeRegion',
        geographic_region=create_geographic_region()
    )
    return administrative_region


def create_mark_of_quality():
    mark_of_quality = MarkOfQuality.objects.create(
        name='TestMarkOfQuality',
        country=create_country(),
        geographic_region=create_geographic_region(),
        administrative_region=create_administrative_region()
    )
    return mark_of_quality


def create_package():
    package = Package.objects.create(
        name='TestPackage',
        country=create_country(),
        geographic_region=create_geographic_region(),
        administrative_region=create_administrative_region(),
        mark_of_quality=create_mark_of_quality()
    )
    return package


class LocationTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

    def test_country_create(self):

        response = self.client.post('/locations/country/create/', {
            'name': 'Test country'
        })

        self.assertRedirects(response, '/locations/country/create/')

    def test_geographic_region_create(self):

        response = self.client.post('/locations/geographic/region/create/', {
            'name': 'Test geographic region',
            'country': create_country()
        })

        self.assertEqual(response.status_code, 200)

    def test_administrative_region_create(self):

        response = self.client.post('/locations/administrative/region/create/', {
            'name': 'Test administrative region',
            'geographic_region': create_geographic_region()
        })

        self.assertEqual(response.status_code, 200)

    def test_mark_of_quality_create(self):

        response = self.client.post('/locations/mark/quality/create/', {
            'name': 'Test mark of quality',
            'country': create_country(),
            'geographic_region': create_geographic_region(),
            'administrative_region': create_administrative_region()
        })

        self.assertEqual(response.status_code, 200)

    def test_package_create(self):

        response = self.client.post(
            '/locations/package/create/', {
                'name': 'Test package',
                'country': create_country(),
                'geographic_region': create_geographic_region(),
                'administrative_region': create_administrative_region(),
                'package': create_package()
            })

        self.assertEqual(response.status_code, 200)


