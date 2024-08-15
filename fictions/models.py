from django.db import models

class Fiction(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title