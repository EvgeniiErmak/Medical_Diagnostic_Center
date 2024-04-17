# educational_resources/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Resource
from django.utils import timezone


class EducationalResourcesTestCase(TestCase):
    def setUp(self):
        # Создание тестового ресурса для проверки представлений
        self.resource = Resource.objects.create(
            title="Test Resource",
            description="A test resource description",
            content="Here is some content",
            video_url="http://example.com/video",
            published_date=timezone.now()
        )

    def test_resource_creation(self):
        # Проверка, что ресурс создан и корректно отображается
        resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(resource.title, "Test Resource")
        self.assertEqual(resource.description, "A test resource description")

    def test_resource_list_view(self):
        # Тест представления списка ресурсов
        response = self.client.get(
            reverse('educational_resources:resources_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Resource")
        self.assertTemplateUsed(
            response, 'educational_resources/resources_list.html')

    def test_resource_detail_view(self):
        # Тест представления детальной информации о ресурсе
        response = self.client.get(
            reverse('educational_resources:resource_detail', args=[self.resource.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Resource")
        self.assertContains(response, "A test resource description")
        self.assertTemplateUsed(
            response, 'educational_resources/resource_detail.html')

    def test_resource_str(self):
        # Тест строкового представления модели
        self.assertEqual(str(self.resource), "Test Resource")
