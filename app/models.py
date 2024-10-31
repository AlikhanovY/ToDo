from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} |  {self.last_name}"


class Item(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}  {self.author.user.username}"
