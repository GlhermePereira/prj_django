# Generated by Django 5.1.1 on 2024-09-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255, unique=True)),
                ("senha", models.CharField(max_length=255)),
            ],
        ),
    ]
