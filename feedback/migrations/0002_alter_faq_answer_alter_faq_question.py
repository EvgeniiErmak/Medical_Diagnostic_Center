# Generated by Django 5.0.4 on 2024-04-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=models.TextField(verbose_name="Ответ"),
        ),
        migrations.AlterField(
            model_name="faq",
            name="question",
            field=models.TextField(verbose_name="Вопрос"),
        ),
    ]