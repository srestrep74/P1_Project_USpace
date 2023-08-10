from django.db import models


class Spaces(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    availability = models.IntegerField(blank=False, null=False)
    clasification = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name