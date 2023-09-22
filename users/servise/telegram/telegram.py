import telebot

bot = telebot.TeleBot('6441221156:AAHVLMCThPNM5Oz3cOs_3iS7Qt4lcW2exu0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот для рассылки напоминаний о твоих привычках.')


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    # Логика подписки пользователя на рассылку напоминаний
    bot.reply_to(message, 'Ты успешно подписался на рассылку напоминаний.')


# Добавьте другие обработчики команд и функции для работы с Telegram

def start_telegram_bot():
    bot.polling(none_stop=True)
