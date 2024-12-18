# Generated by Django 5.1.4 on 2024-12-18 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expenses",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("ONLINE_SERVICES", "ONLINE_SERVICES"),
                            ("TRAVEL", "TRAVEL"),
                            ("FOOD", "FOOD"),
                            ("RENT", "RENT"),
                            ("OTHERS", "OTHERS"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, max_length=255
                    ),
                ),
                ("description", models.TextField()),
                ("date", models.DateField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]