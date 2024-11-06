from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    fecha_medicion = models.DateField(null=True, blank=True)
    medicion_completa = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["completo"]


