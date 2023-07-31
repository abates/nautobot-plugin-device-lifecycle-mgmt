# Generated by Django 3.2.16 on 2023-04-20 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_device_lifecycle_mgmt", "0009_software_remove_image_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="softwareimagelcm",
            name="hashing_algorithm",
            field=models.CharField(blank=True, default="", max_length=32),
        ),
    ]
