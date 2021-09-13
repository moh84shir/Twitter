from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class MessageManager(models.Manager):
    def get_my_messages(self, to_user, from_user):
        lookup = (
            Q(to_user=to_user) |
            Q(from_user=from_user)
        )

        return self.get_queryset().filter(lookup)



class Messages(models.Model):
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    text = models.TextField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    time = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return self.title