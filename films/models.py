from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    bio = models.TextField()
    photo = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, related_name='movie_ratings', null=True)
    rating = models.ForeignKey(RatingStar, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} ({self.rating})'


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    age = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='directors/')

    def __str__(self):
        return self.name


class MovieActor(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.actor.name} в роли {self.role} в фильме {self.movie.title}'


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    release_date = models.DateField(default=date.today)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='director')
    descriptions = models.TextField()
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, related_name='actor', null=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title






