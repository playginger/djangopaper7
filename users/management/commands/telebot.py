from django.core.management.base import BaseCommand

from users.servise.telegram.telegram import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.polling(none_stop=True)
