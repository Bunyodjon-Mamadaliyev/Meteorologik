from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.profile = Profile.objects.create(user=self.user, organization='Test Org', role='moderator')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.organization, 'Test Org')
        self.assertEqual(self.profile.role, 'moderator')

    def test_default_values(self):
        new_user = User.objects.create_user(username='newuser', password='newpass123')
        new_profile = Profile.objects.create(user=new_user)
        self.assertEqual(new_profile.organization, 'Default Organization')
        self.assertEqual(new_profile.role, 'user')

    def test_str_method(self):
        self.assertEqual(str(self.profile), 'testuser profili')

    def test_verbose_names(self):
        self.assertEqual(Profile._meta.verbose_name, "Foydalanuvchi profili")
        self.assertEqual(Profile._meta.verbose_name_plural, "Foydalanuvchi profillari")
