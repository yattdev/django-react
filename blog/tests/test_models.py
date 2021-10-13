from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher


class CustomUserTests(TestCase):
    """ DocString for CustomUserTests """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="yattara",
            email="yatt@gmail.com",
            password=make_password("yatt_test123"),
        )

        self.assertEqual(user.username, "yattara")
        self.assertEqual(user.email, "yatt@gmail.com")
        self.assertTrue(user.check_password("yatt_test123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@email.com",
            password="adminpass123",
        )

        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.email, "admin@email.com")
        self.assertTrue(admin_user.check_password("adminpass123"))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        
