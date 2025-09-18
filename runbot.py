import os
import telebot
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_system.settings')
django.setup()

from notification.models import UserProfile


TELEGRAM_BOT_TOKEN = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')

if not TELEGRAM_BOT_TOKEN:
    print("Бот-заглушка запущен (без реального токена)")
    print("Для реальной работы добавьте TELEGRAM_BOT_TOKEN в settings.py")
    while True:
        input("Нажмите Enter для выхода...")
        break

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    try:
        user = UserProfile.objects.first()
        user.telegram_chat_id = chat_id
        user.save()
        bot.reply_to(message, f"Вы подписаны на уведомления! Ваш ID: {chat_id}")
        print(f"Сохранен chat_id {chat_id} для {username}")
    except UserProfile.DoesNotExist:
        bot.reply_to(message, "Пользователь не найден в системе")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling()
