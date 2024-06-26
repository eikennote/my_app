# Generated by Django 5.1.dev20240318084533 on 2024-04-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keiba_app', '0002_race_description_alter_race_ground_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horse_name', models.CharField(max_length=12, verbose_name='馬名')),
                ('recommend', models.IntegerField(default=0, verbose_name='おすすめ度')),
                ('horse_age', models.IntegerField(default=2, verbose_name='馬齢')),
                ('description', models.TimeField(max_length=1000, null=True, verbose_name='説明')),
            ],
        ),
    ]
