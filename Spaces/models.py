from django.db import models

# Create your models here.
from django.db import models
from Admins.models import *
from Auth.models import *


class Reminder(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE)
    remember_to = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    RATINGS = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    rating = models.IntegerField(choices=RATINGS)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.rating)