from django.db import models
from .game import Game


class Review(models.Model):
    number_rating = models.PositiveIntegerField()
    comment = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review {self.id} for {self.game.title}"
