from django.db import models
from spaces.models import Spaces

class OcuppiedSpaces(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    space_id = models.ForeignKey(Spaces, on_delete=models.CASCADE)
    occupied_at = models.DateTimeField(auto_now_add=True)
    unoccupied_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)