# educational_resources/models.py

from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # Для видео или внешних ссылок можно использовать URLField
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
