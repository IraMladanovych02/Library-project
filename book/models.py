from django.db import models


class Book(models.Model):
    class StatusChoices(models.TextChoices):
        SOFT = "Soft"
        HARD = "Hard"
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=255, choices=StatusChoices.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f" {self.title} by {self.author}"


