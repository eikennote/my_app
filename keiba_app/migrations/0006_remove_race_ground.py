# Generated by Django 5.1.dev20240318084533 on 2024-04-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keiba_app', '0005_evidence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='ground',
        ),
    ]
