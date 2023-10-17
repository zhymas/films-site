from django.contrib import admin
from .models import Movie, Rating, RatingStar, Actor, Genre, Director, MovieActor

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(MovieActor)
