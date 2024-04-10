# educational_resources/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resource
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


@receiver(post_save, sender=Resource)
def resize_image(sender, instance, **kwargs):
    if instance.image:
        img = Image.open(instance.image)
        output_size = (800, 450)  # Желаемый размер изображения
        img.thumbnail(output_size)
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        instance.image.save(instance.image.name, ContentFile(buffer.getvalue()), save=False)
