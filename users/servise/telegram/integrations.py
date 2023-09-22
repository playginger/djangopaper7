import telebot


def send_telegram_notification(habit):
    bot_token = '6441221156:AAHVLMCThPNM5Oz3cOs_3iS7Qt4lcW2exu0'
    chat_id = 'YOUR_TELEGRAM_CHAT_ID'
    message = f"Reminder: {habit.name} - {habit.description}"

    bot = telebot.TeleBot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)
