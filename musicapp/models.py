from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Artiste (models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    age =  models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name


class Song (models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateTimeField(auto_now_add=True)
    likes =  models.IntegerField(max_length=255)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyric (models.Model):
    content = models.TextField(max_length=10000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id.title +" lyric"

