# Generated by Django 5.0.4 on 2024-04-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_customuser_address_customuser_country_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="diagnostic_history",
            field=models.TextField(blank=True, verbose_name="История диагностик"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="medical_data",
            field=models.TextField(blank=True, verbose_name="Медицинские данные"),
        ),
    ]