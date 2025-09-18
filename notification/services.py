import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from django.conf import settings


class NotificationService:
    def __init__(self):
        self.services = ['email', 'telegram', 'sms']

    def send_notification(self, user_profile, message, subject=None):
        """Основной метод отправки уведомления с запасными вариантами"""

        for service in self.services:
            try:
                if service == 'email' and user_profile.user.email:
                    if self._send_email(user_profile.user.email, subject, message):
                        return True
                elif service == 'telegram' and user_profile.telegram_chat_id:
                    if self._send_telegram(user_profile.telegram_chat_id, message):
                        return True
                elif service == 'sms' and user_profile.phone:
                    if self._send_sms(user_profile.phone, message):
                        return True

            except Exception as e:
                print(f"Ошибка отправки через {service}: {e}")
                continue

        return False

    def _send_email(self, email, subject, message):
        if not all([settings.EMAIL_HOST, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD]):
            print("Отсутствуют настройки для Email")
            return False

        try:
            msg = MIMEMultipart()
            msg['From'] = settings.DEFAULT_FROM_EMAIL
            msg['To'] = email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain', 'utf-8'))

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)

            print(f"Email отправлен на {email}")
            return True

        except Exception as e:
            print(f"Ошибка отправки email: {e}")
            return False

    def _send_sms(self, phone, message):
        """Отправка SMS (заглушка)"""
        try:
            print(f"SMS отправлено на {phone}: {message}")
            return True
        except Exception as e:
            print(f"Ошибка отправки SMS: {e}")
            return False

    def _send_telegram(self, chat_id, message):
        """Отправка сообщения в Telegram"""
        try:
            if hasattr(settings, 'TELEGRAM_BOT_TOKEN'):
                url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    print(f"Telegram сообщение отправлено в чат {chat_id}")
                    return True
            else:
                print("Отсутствует токен бота")
            return False

        except Exception as e:
            print(f"Ошибка отправки Telegram: {e}")
            return False
