from django.db import models
from .game import Game
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"Review {self.id} for {self.game.title}"
