from django.db import models
from .game import Game
from .image import Image


class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
