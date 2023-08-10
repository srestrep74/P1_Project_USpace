from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    account_type = models.IntegerField(editable=False)

    def __str__(self):
        return self.name