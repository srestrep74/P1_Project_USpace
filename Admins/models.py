from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
from django.db import models
>>>>>>> sebas

class Space(models.Model):
    AVAILABILITY = (
        (0, 'Disponible'),
        (1, 'Ocupado'),
        (2, 'Deshabilitado')
    )
    CLASSIFICATION = (
        (0, 'Escenario deportivo'),
        (1, 'Mesa de restaurante'),
        (2, 'Zona de descanso')
    )

    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    availability = models.IntegerField(blank=False, null=False, choices=AVAILABILITY)
<<<<<<< HEAD
    classification = models.IntegerField(blank=False, null=False, choices=CLASSIFICATION)

=======
    classification = models.IntegerField(blank=False, null=False, choices=CLASIFICATION)
    latitude = models.FloatField(null=True)
    longitude= models.FloatField(null=True)
    image = models.ImageField(null=True)
>>>>>>> sebas
    def __str__(self):
        return self.name