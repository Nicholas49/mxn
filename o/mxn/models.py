from django.db import models
from django.utils import timezone


class Morty(models.Model):
    name = models.CharField(max_length=20)
    commont = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)
