from django.db import models
from django.contrib.auth.models import User


class staff(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return str(self.username)