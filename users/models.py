from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError

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

    def save(self, *args, **kwargs):
        if self.is_rewarding and self.related_habit is not None:
            raise ValidationError("Невозможно выбрать одновременно связанную привычку и награду.")
        if self.estimated_duration > 120:
            raise ValidationError("Время не должно превышать 120 секунд.")
        if self.is_rewarding and self.reward:
            raise ValidationError("Невозможно указать вознаграждение за полезную привычку.")
        if self.is_rewarding and self.related_habit:
            raise ValidationError("Сопутствующая привычка не может быть указана как полезная привычка.")
        if self.periodicity < 7:
            raise ValidationError("Привычку нельзя выполнять реже, чем раз в 7 дней.")

        super().save(*args, **kwargs)
