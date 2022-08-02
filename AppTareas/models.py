from django.db import models

# Create your models here.

class Tareas(models.Model):
    nombre = models.CharField('Nombre', max_length = 50)
    contenido = models.CharField('Contenido', max_length = 150)
    completada = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
    
    def __str__(self):
        return 'ID: ' + (str(self.id)) + ' Nombre: ' + self.nombre