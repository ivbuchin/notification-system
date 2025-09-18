# setup_db.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_system.settings')
django.setup()

from django.contrib.auth.models import User
from notification.models import UserProfile

# Создаем тестового пользователя
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)

profile = UserProfile.objects.create(
    user=user,
    phone='+79123456789',
)

print("Тестовые данные созданы")
