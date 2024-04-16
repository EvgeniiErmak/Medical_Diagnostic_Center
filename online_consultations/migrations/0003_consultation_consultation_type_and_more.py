# Generated by Django 5.0.4 on 2024-04-15 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0005_alter_appointmentslot_specialist"),
        ("clinic", "0003_specialist_age"),
        ("online_consultations", "0002_remove_consultation_datetime_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="consultation",
            name="consultation_type",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="specialist",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="consultations",
                to="clinic.specialist",
            ),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="patient",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="slot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultations",
                to="appointments.appointmentslot",
            ),
        ),
    ]