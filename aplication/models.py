from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    comision = models.IntegerField(blank=False)
    
    def __str__(self):
        return f"{self.nombre}"

class Carrera(models.Model):
    comision = models.IntegerField()
    nombre = models.CharField(max_length=50, blank=False)
    duracion = models.PositiveSmallIntegerField(default=5, blank=False)
    
    def __str__(self):
        return f'{self.nombre}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"