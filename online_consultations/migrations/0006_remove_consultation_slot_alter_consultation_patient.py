# Generated by Django 5.0.4 on 2024-04-15 21:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_consultations", "0005_alter_consultation_consultation_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="consultation",
            name="slot",
        ),
        migrations.AlterField(
            model_name="consultation",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
