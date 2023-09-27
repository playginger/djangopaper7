from celery import shared_task
from .models import Habit
from users.servise.telegram.integrations import send_telegram_notification

@shared_task
def send_notification(habit_id):
    # Получение привычки по идентификатору
    habit = Habit.objects.get(id=habit_id)
    # Отправка уведомления в Telegram
    send_telegram_notification(habit)

