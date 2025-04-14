from django.test import TestCase
from django.contrib.auth import get_user_model
from station.models import Station
from weather.models import Weather
from django.utils import timezone

User = get_user_model()

class WeatherModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.station = Station.objects.create(
            name='Test Station',
            latitude=41.3111,
            longitude=69.2797,
            created_by=self.user
        )
        self.weather = Weather.objects.create(
            station=self.station,
            timestamp=timezone.now(),
            temperature=25.5,
            humidity=60.2,
            pressure=1013.25,
            wind_speed=5.3,
            wind_direction=180.0,
            precipitation=0.0,
            created_by=self.user
        )

    def test_weather_creation(self):
        self.assertEqual(self.weather.station, self.station)
        self.assertEqual(self.weather.created_by, self.user)
        self.assertEqual(float(self.weather.temperature), 25.5)
        self.assertEqual(float(self.weather.humidity), 60.2)
        self.assertEqual(float(self.weather.pressure), 1013.25)
        self.assertEqual(float(self.weather.wind_speed), 5.3)
        self.assertEqual(float(self.weather.wind_direction), 180.0)
        self.assertEqual(float(self.weather.precipitation), 0.0)

    def test_weather_str(self):
        expected_str = f"{self.station.name} - {self.weather.timestamp}"
        self.assertEqual(str(self.weather), expected_str)
