import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_system.settings')
django.setup()

from notification.models import UserProfile
from notification.services import NotificationService


def main():
    try:
        email = input('Введите email: ')
        user_profile = UserProfile.objects.first()
        user_profile.user.email = email
        user_profile.save()
        if user_profile:
            service = NotificationService()
            success = service.send_notification(user_profile, "Тестовое уведомление!")
            print("Отправлено!" if success else "Ошибка!")
        else:
            print("Нет пользователей в БД")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
