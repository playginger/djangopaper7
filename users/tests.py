from django.test import TestCase
from rest_framework.test import APIClient

from users.models import User, Habit


class HabitTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            name='admin@sky.pro',
            description='Admin',
            is_public=True,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('123qwe456rty')
        user.save()
        self.user = user
        self.habit = Habit.objects.create(user=self.user, location='Test', time='12:00:00', action='test action',
                                          reward='test reward')
        self.client = APIClient()

    def test_view_habit(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, 200)

    def test_list_habit(self):
        self.client.force_authenticate(self.user)
        # lesson = Habit.objects.create(title='Test Lesson', description=self.course)
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, 200)

    def test_delete_habit(self):
        self.client.force_authenticate(self.user)
        habit = Habit.objects.create(user=self.user, location='Test', time='12:00:00', action='test action',
                                     reward='test reward')
        response = self.client.delete(f'habits/delete/{habit.id}/')
        self.assertEqual(response.status_code, 204)
