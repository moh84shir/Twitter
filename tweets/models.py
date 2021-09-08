from django.db import models
from django.contrib.auth.models import User


# data base models for tweets
class Tweet(models.Model):
    """ Tweet Model """
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title
