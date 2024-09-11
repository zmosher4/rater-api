from django.db import models


class Image(models.Model):
    game_img = models.ImageField(upload_to='game_images/')

    def __str__(self):
        return f"Image {self.id}"
