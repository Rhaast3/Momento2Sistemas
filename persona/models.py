from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)  # dni unico
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos} - {self.dni} - {self.rol}'

    class Meta:
        db_table = 'persona'
