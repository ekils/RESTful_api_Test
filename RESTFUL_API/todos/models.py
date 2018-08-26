from django.db import models


class Todo(models.Model):
    account = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)


    def __str__(self):
        """A string representation of the model."""
        return self.account