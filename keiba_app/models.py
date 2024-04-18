from django.db import models

# Create your models here.
class Race(models.Model):
    grass_or_dirt = (
        ('grass', '芝'),
        ('dirt', 'ダート'),
    )
    race_date = models.DateField(verbose_name='レース日時')
    race_name = models.CharField(max_length=30, verbose_name='レース名')
    race_distance = models.IntegerField(default=0, verbose_name='レース距離')
    ground = models.CharField(default='grass', max_length=5, choices=grass_or_dirt, verbose_name='馬場情報')
    description = models.TextField(max_length=1000, null=True, verbose_name='説明')

    def __str__(self):
        return self.name
    

class Horse(models.Model):
    horse_name = models.CharField(max_length=12, verbose_name='馬名')
    recommend = models.IntegerField(default=0, verbose_name='おすすめ度')
    horse_age = models.IntegerField(default=2, verbose_name='馬齢')
    description = models.TextField(max_length=1000, null=True, verbose_name='説明')

    def __str__(self):
        return self.name
    

class Evidence(models.Model):
    description = models.TextField(max_length=1000, null=True, verbose_name='説明')

    def __str__(self):
        return self.name
