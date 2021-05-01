from django.db import models


class Post(models.Model):
    """ Post as a model. """
    text = models.TextField()

    def __str__(self):
        return str(self.text[:50])
