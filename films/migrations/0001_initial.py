# Generated by Django 4.1.7 on 2023-10-17 19:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='actors/')),
                ('url', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('age', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='directors/')),
                ('url', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('url', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('descriptions', models.TextField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
                ('url', models.SlugField(max_length=100)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='films.director')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.genre')),
            ],
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_ratings', to='films.movie')),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.ratingstar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=100)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie')),
            ],
        ),
    ]
