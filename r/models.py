from django.db import models

# Create your models here.


class Subreddit(models.Model):
    name = models.CharField(max_length=100)


class ImageObject(models.Model):
    sub = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    caption = models.CharField(max_length=500)

