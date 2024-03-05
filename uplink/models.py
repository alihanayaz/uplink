from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=64, blank=True)
    location = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=64)
    url = models.URLField()
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()