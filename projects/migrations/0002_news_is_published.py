# Generated by Django 4.2 on 2025-03-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
    ]
