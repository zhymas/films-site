from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    Bio = models.TextField()
    photo = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    release_date = models.DateField(default=date.today)
    director = models.CharField(max_length=255)
    descriptions = models.TextField()
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, related_name='actor')
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    rating = models.DecimalField()

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.ForeignKey(RatingStar, models.SET_NULL, related_name='rating')

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} ({self.rating})'


