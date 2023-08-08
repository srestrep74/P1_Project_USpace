from django.db import models


class Space(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    availability = models.IntegerField(blank=False, null=False)
    clasification = models.IntegerField(blank=False, null=False)


class OcuppiedSpace(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE)
    occupied_at = models.DateTimeField(auto_now_add=True)
    unoccupied_at = models.DateTimeField(auto_now=True)