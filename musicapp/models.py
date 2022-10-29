from django.db import models

# Create your models here.


class Artiste (models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    age =  models.CharField(max_length=255)
class Song (models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateTimeField(auto_now_add=True)
    likes =  models.IntegerField(max_length=255)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
class Lyric (models.Model):
    content = models.CharField(max_length=255)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

