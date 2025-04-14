from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Station

class StationAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.station = Station.objects.create(
            name='Test name',
            station_id='Test station_id',
            latitude=41.311081,
            longitude=69.3,
            elevation=123.45,
            is_active=True,
            created_by=self.user,
        )
        self.url = reverse('station-detail', kwargs={
            'pk': self.station.pk
        })

    def test_get_station(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test name')
        self.assertEqual(response.data['station_id'], 'Test station_id')
        self.assertEqual(float(response.data['latitude']), 41.311081)
        self.assertEqual(float(response.data['longitude']), 69.3)
        self.assertEqual(float(response.data['elevation']), 123.45)
        self.assertEqual(response.data['is_active'], True)
        self.assertEqual(response.data['created_by'], self.user.username)