from django.contrib.auth.models import User
from django.test import TestCase, Client

from location.models import (
    Country, GeographicRegion,
    AdministrativeRegion,
    MarkOfQuality
)


class LocationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country = Country.objects.create(name='TestCountry')
        cls.geographic_region = GeographicRegion.objects.create(
            name='TestGeographicRegion',
            country=cls.country
        )
        cls.administrative_region = AdministrativeRegion.objects.create(
            name='TestAdministrativeRegion',
            geographic_region=cls.geographic_region
        )
        cls.mark_of_quality = MarkOfQuality.objects.create(
            name='TestMarkOfQuality',
            country=cls.country,
            geographic_region=cls.geographic_region,
            administrative_region=cls.administrative_region
        )

    @staticmethod
    def make_user(username, email, password):
        user = User.objects.create_superuser(username, email, password)
        return user

    def setUp(self):
        username, email, password = 'admin', 'email@gmail.com', 'secret'
        self.user = self.make_user(username, email, password)

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
                'country': self.country
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create geographic region

        response = self.authenticated_client.post(
            url, {
                'name': 'Test geographic region',
                'country': self.country
            })

        self.assertEqual(response.status_code, 200)

    def test_administrative_region_create(self):
        url = '/locations/administrative/region/create/'
        # Anonymous users can't create administrative region

        response = self.client.post(
            url, {
                'name': 'Test administrative region',
                'geographic_region': self.geographic_region
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create administrative region

        response = self.authenticated_client.post(
            url, {
                'name': 'Test administrative region',
                'geographic_region': self.geographic_region

            })

        self.assertEqual(response.status_code, 200)

    def test_mark_of_quality_create(self):
        url = '/locations/mark/quality/create/'
        # Anonymous users can't create  mark of quality

        response = self.client.post(
            url, {
                'name': 'Test mark of quality',
                'country': self.country,
                'geographic_region': self.geographic_region,
                'administrative_region': self.administrative_region
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create mark of quality

        response = self.authenticated_client.post(
            url, {
                'name': 'Test mark of quality',
                'country': self.country,
                'geographic_region': self.geographic_region,
                'administrative_region': self.administrative_region
            })

        self.assertEqual(response.status_code, 200)

    def test_package_create(self):
        url = '/locations/package/create/'
        # Anonymous users can't create package

        response = self.client.post(
            url, {
                'name': 'Test package',
                'country': self.country,
                'geographic_region': self.geographic_region,
                'administrative_region': self.administrative_region,
                'mark_of_quality': self.mark_of_quality
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'/login/?next={url}')

        # Authenticated users can create package

        response = self.authenticated_client.post(
            url, {
                'name': 'Test package',
                'country_id': self.country,
                'geographic_region_id': self.geographic_region,
                'administrative_region_id': self.administrative_region,
                'mark_of_quality_id': self.mark_of_quality
            })

        self.assertEqual(response.status_code, 200)