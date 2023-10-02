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
    RATINGS = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    rating = models.IntegerField(choices=RATINGS)
    space = models.ForeignKey(Space,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE )
    comment = models.CharField(max_length=500)
    create_date = models.DateField(null=True,auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class Rating(models.Model):
    value = models.PositiveIntegerField()