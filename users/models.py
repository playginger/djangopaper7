from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    pass


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    time = models.TimeField()
    action = models.CharField(max_length=200)
    is_rewarding = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    periodicity = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=200)
    estimated_duration = models.PositiveIntegerField(default=2)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.action