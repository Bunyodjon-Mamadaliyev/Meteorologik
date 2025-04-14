from django.test import TestCase
from django.contrib.auth.models import User
from .models import Export
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone


class ExportModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='exportuser', password='testpass123')
        self.export = Export.objects.create(
            user=self.user,
            export_type='csv',
            status='completed',
            file=SimpleUploadedFile("export.csv", b"header1,header2\nvalue1,value2"),
            completed_at=timezone.now()
        )

    def test_export_creation(self):
        self.assertEqual(self.export.user.username, 'exportuser')
        self.assertEqual(self.export.export_type, 'csv')
        self.assertEqual(self.export.status, 'completed')
        self.assertIsNotNone(self.export.file)

    def test_default_status(self):
        export2 = Export.objects.create(user=self.user, export_type='json')
        self.assertEqual(export2.status, 'pending')

    def test_str_method(self):
        expected_str = f"{self.user.username} - CSV (Yakunlandi)"
        self.assertEqual(str(self.export), expected_str)

    def test_verbose_names(self):
        self.assertEqual(Export._meta.verbose_name, "Ma'lumotlar eksporti")
        self.assertEqual(Export._meta.verbose_name_plural, "Ma'lumotlar eksportlari")

    def test_ordering(self):
        export2 = Export.objects.create(user=self.user, export_type='json')
        exports = Export.objects.all()
        self.assertEqual(exports[0], export2)
