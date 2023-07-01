from django.db import models
import time

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    image = models.CharField(max_length=500, default='default.jpg')
    info = models.TextField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Song(models.Model):
    title = models.CharField(max_length=250)
    length = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title

    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))


class Playlist(models.Model):
    title = models.CharField(max_length=150)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title