import os
from celery import Celery

# Устанавливаем окружение Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Настраиваем Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическая загрузка задач из приложений
app.autodiscover_tasks()