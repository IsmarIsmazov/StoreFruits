import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE перед импортом Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

# Инициализируйте Django
django.setup()

from django.contrib.auth.models import User

# Создайте суперпользователя, если он не существует
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
