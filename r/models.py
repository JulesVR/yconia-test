from django.db import models
import praw

# Create your models here.


class Subreddit(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=1000, default='https://i.imgur.com/NqomU87s.png')
    time_ago_of_last_update = models.CharField(max_length=10, default='0')
    #tag = models.CharField(max_length=100)
    #is_popular = models.Boolean(default = false)
    #caption_on = models.Boolean(default = true)


class ImageObject(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    sub = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=1000)
    caption = models.TextField(max_length=5000)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    #id_nb = models.IntegerField(default=0)

    def __str__(self):
        return self.url

