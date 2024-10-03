from django.db import models
from .game import Game
from .image import Image


class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='pictures')
    action_pic = models.ImageField(
        upload_to='actionimages',
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )
