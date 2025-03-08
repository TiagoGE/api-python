from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

#To print a string version of the book object if we need to debug
    def __str__(self):
        return self.title