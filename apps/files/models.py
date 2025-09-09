
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('processed', 'Processed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    line_count = models.IntegerField(default=0, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.line_count and self.status == 'processed':
            # Подсчёт строк будет выполняться в Celery
            pass
        super().save(*args, **kwargs)
