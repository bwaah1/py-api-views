from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    actor = models.ManyToManyField(
        Actor,
        related_name="movies"
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="movies"
    )
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
