from django.db import models

class Turno(models.Model):
    
    cancha = models.CharField(max_length=50)
    reserva = models.BooleanField(default=False)
