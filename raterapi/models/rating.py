from django.db import models
from .game import Game
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")
