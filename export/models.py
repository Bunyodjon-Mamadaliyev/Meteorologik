from django.db import models
from django.contrib.auth.models import User

class Export(models.Model):
    EXPORT_TYPE_CHOICES = [
        ('csv', 'CSV'),
        ('json', 'JSON'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('completed', 'Yakunlandi'),
        ('failed', 'Xatolik'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_exports')
    export_type = models.CharField(max_length=10, choices=EXPORT_TYPE_CHOICES)
    file = models.FileField(upload_to='data_exports/%Y/%m/%d/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_export_type_display()} ({self.get_status_display()})"

    class Meta:
        verbose_name = 'Ma\'lumotlar eksporti'
        verbose_name_plural = 'Ma\'lumotlar eksportlari'
        ordering = ['-created_at']
