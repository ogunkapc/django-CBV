from turtle import title
from django.db import models

# Create your models here.
class TodoApp(models.Model):
    #fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    #rename the instances of the model
    # with their title name
    def __str__(self):
        return self.title