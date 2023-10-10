from django.db import models
from django.contrib.auth.models import User


class user_m(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default='profile.jpg', null=True)
    def __str__(self):
        return str(self.username)