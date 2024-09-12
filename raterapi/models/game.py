from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    year_released = models.PositiveIntegerField()
    number_of_players = models.PositiveIntegerField()
    game_length_hrs = models.PositiveIntegerField()
    age_rec = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    categories = models.ManyToManyField(
        "Category", through='GameCategory', related_name="games"
    )

    def __str__(self):
        return self.title
