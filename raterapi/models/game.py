from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    year_released = models.PositiveIntegerField()
    number_of_players = models.PositiveIntegerField()
    game_length_hrs = models.PositiveIntegerField()
    age_rec = models.PositiveIntegerField()

    def __str__(self):
        return self.title
