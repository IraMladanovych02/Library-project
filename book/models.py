from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class StatusChoices(models.TextChoices):
        SOFT = "Soft"
        HARD = "Hard"
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)
    cover = models.CharField(max_length=255, choices=StatusChoices.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, upload_to="movie_image_path")

    def __str__(self):
        return f" {self.title} {self.author}"


