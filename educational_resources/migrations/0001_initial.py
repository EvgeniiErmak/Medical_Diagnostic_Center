# Generated by Django 5.0.4 on 2024-04-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("video_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
