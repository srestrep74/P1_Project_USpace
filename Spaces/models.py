from django.db import models
from Admins.models import *
from Auth.models import *


class Notification(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    remember_to = models.DateTimeField()
    sent = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    rating = models.IntegerField(null=False, default=0)
    space = models.ForeignKey(Space,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE )
    comment = models.CharField(max_length=500)
    create_date = models.DateField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.rating)
    

class Damage(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    space_name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='damages/images', null=False, blank=False)
    solved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.space_name)