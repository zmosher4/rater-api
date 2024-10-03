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

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        ratings_num = 0
        for rating in ratings:
            total_rating += rating.rating
            ratings_num += 1
        avg_rating = total_rating / ratings_num

        return avg_rating

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.

        # return the result
