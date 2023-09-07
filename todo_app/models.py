from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    
class Rating(models.Model):
    value = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
