# Generated by Django 4.2.3 on 2024-04-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="resolved_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]