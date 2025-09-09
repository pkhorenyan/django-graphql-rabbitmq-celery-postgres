from celery import shared_task
from django.core.files.storage import default_storage
from .models import File

@shared_task
def process_file(file_id):
    try:
        file_instance = File.objects.get(id=file_id)
        file_instance.status = 'processing'
        file_instance.save()

        # Открываем файл в бинарном режиме
        file_path = file_instance.file.path
        with default_storage.open(file_path, 'rb') as f:
            content = f.read().decode('utf-8')  # Читаем байты и декодируем в строку

        # Подсчитываем строки
        line_count = len(content.splitlines())

        # Обновляем модель
        file_instance.line_count = line_count
        file_instance.status = 'processed'
        file_instance.save()
    except Exception as e:
        file_instance.status = 'pending'  # Возвращаем в ожидание при ошибке
        file_instance.save()
        raise e