# educational_resources/models.py

from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    # Дополнительно можно добавить поле для хранения файла или ссылки на видео
    # file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    # video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
