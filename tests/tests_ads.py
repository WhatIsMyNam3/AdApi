from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase

from apps.ads.models import Ad


class AdListTests(APITestCase):
    def setUp(self) -> None:
        self.ad1 = Ad.objects.create(
            title='TEST1',
            ad_id=12345678,
            author='TEST1',
            views=12345,
            position=1
        )
        self.ad2 = Ad.objects.create(
            title='TEST2',
            ad_id=87654321,
            author='TEST2',
            views=54321,
            position=2
        )

    def test_get_ad_list(self):
        url = reverse('ad-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class AdDetailTests(APITestCase):
    def setUp(self) -> None:
        self.data = {
            'title': 'TEST1',
            'ad_id': 12345678,
            'author': 'TEST1',
            'views': 12345,
            'position': 1
        }
        self.ad1 = Ad.objects.create(
            title=self.data['title'],
            ad_id=self.data['ad_id'],
            author=self.data['author'],
            views=self.data['views'],
            position=self.data['position']
        )

    def test_get_ad_detail(self):
        url = reverse('ad-detail', args=[self.ad1.ad_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        for field, value in self.data.items():
            with self.subTest(field=field):
                self.assertEqual(getattr(self.ad1, field), value)

    def test_get_not_exist_ad(self):
        url = reverse('ad-detail', args=[52])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
