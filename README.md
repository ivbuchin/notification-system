## Настройка окружения

Установите зависимости:
```bash
pip install -r requirements.txt
```

Создайте файл `.env` и заполните
следующие настройки:

```bash
EMAIL_HOST=...
EMAIL_PORT=...
EMAIL_USE_TLS=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...

TELEGRAM_BOT_TOKEN=...
```

Выполните миграции:
```bash
python manage.py migrate
```

Создайте тестовые данные:
```bash
python setup_db.py
```

Запустите бота:
```bash
python manage.py runbot.py
```

Отправьте боту сообщение `/start`

Запустите проверку отправки уведомлений:
```bash
python send_test.py
```