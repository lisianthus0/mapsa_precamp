from django.db import models
from django.urls import reverse

class Todo(models.Model):
    job = models.CharField(max_length=100)
    date = models.DateTimeField()
    body = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.job}"

