# educational_resources/models.py

from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # Для видео по ссылке
    video_file = models.FileField(
        upload_to='videos/', null=True, blank=True)  # Для локального видео
    image = models.ImageField(
        upload_to='resources_images/', null=True, blank=True)

    def __str__(self):
        return self.title
