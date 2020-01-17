from django.contrib.auth.models import User
from django.test import TestCase, Client

from location.models import (
    Country, GeographicRegion,
    AdministrativeRegion,
    MarkOfQuality
)


def create_country():
    country = Country.objects.create(name='Test Country')
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


class LocationTestCase(TestCase):
    def setUp(self):
        super().setUp()

        username, password = 'admin', 'secret'
        User.objects.create_user(username=username, password=password)

        self.authenticated_client = Client()
        self.authenticated_client.login(username=username, password=password)

        self.client = Client()

    def test_country_create(self):
        url = '/locations/country/create/'
        # Anonymous users can't create country

        response = self.client.post(
            url, {
                'name': 'Country test'
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create country

        response = self.authenticated_client.post(
            url, {
                'name': 'Country test'
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    def test_geographic_region_create(self):
        url = '/locations/geographic/region/create/'
        # Anonymous users can't create geographic region

        response = self.client.post(
            url, {
                'name': 'Test geographic region',
                'country': create_country()
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create geographic region

        response = self.authenticated_client.post(
            url, {
                'name': 'Test geographic region',
                'country': create_country()
            })

        self.assertEqual(response.status_code, 200)

    def test_administrative_region_create(self):
        url = '/locations/administrative/region/create/'
        # Anonymous users can't create administrative region

        response = self.client.post(
            url, {
                'name': 'Test administrative region',
                'geographic_region': create_geographic_region()
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create administrative region

        response = self.authenticated_client.post(
            url, {
                'name': 'Test administrative region',
                'geographic_region': create_geographic_region()
            })

        self.assertEqual(response.status_code, 200)

    def test_mark_of_quality_create(self):
        url = '/locations/mark/quality/create/'
        # Anonymous users can't create  mark of quality

        response = self.client.post(
            url, {
                'name': 'Test mark of quality',
                'country': create_country(),
                'geographic_region': create_geographic_region(),
                'administrative_region': create_administrative_region()
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create mark of quality

        response = self.authenticated_client.post(
            url, {
                'name': 'Test mark of quality',
                'country': create_country(),
                'geographic_region': create_geographic_region(),
                'administrative_region': create_administrative_region()
            })

        self.assertEqual(response.status_code, 200)

    def test_package_create(self):
        url = '/locations/package/create/'
        # Anonymous users can't create package

        response = self.client.post(
            url, {
                'name': 'Test package',
                'country': create_country(),
                'geographic_region': create_geographic_region(),
                'administrative_region': create_administrative_region(),
                'mark_of_quality': create_mark_of_quality()
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create package

        response = self.authenticated_client.post(
            url, {
                'name': 'Test package',
                'country_id': create_country(),
                'geographic_region_id': create_geographic_region(),
                'administrative_region_id': create_administrative_region(),
                'mark_of_quality_id': create_mark_of_quality(),
            })

        self.assertEqual(response.status_code, 200)
