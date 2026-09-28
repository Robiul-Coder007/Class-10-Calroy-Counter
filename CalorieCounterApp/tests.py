from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileTest(TestCase):

    def test_male_bmr(self):

        user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        profile = UserProfile.objects.create(
            user=user,
            name='Test User',
            age=25,
            gender='Male',
            height=170,
            weight=65
        )

        expected = round(
            66.47
            + (13.75 * 65)
            + (5.003 * 170)
            - (6.755 * 25),
            2
        )

        self.assertEqual(
            profile.calculate_bmr(),
            expected
        )