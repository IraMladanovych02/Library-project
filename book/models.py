from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)
