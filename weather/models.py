from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Weather(models.Model):
    station = models.ForeignKey('station.Station', on_delete=models.CASCADE, related_name='weather_data')
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=6, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.DecimalField(max_digits=5,  decimal_places=2,  validators=[MinValueValidator(0), MaxValueValidator(360)])
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Ob-havo ma'lumoti"
        verbose_name_plural = "Ob-havo ma'lumotlari"

    def __str__(self):
        return f"{self.station.name} - {self.timestamp}"
