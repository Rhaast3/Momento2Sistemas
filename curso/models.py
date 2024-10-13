from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_max = models.IntegerField()
    profesor = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    
    # Cambiar el related_name para evitar conflicto con otros modelos
    estudiantes = models.ManyToManyField(Persona, related_name='cursos_estudiante', blank=True)  
    
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def clean(self):
        if self.capacidad_max <= 0:
            raise ValidationError('La capacidad máxima debe ser mayor a 0.')
        
        if self.profesor and self.profesor.rol != 'Profesor':
            raise ValidationError('La persona asignada debe tener el rol "Profesor".')

    def __str__(self) -> str:
        return f'{self.nombre} - {self.capacidad_max} - {self.profesor.nombre} - {self.profesor.apellidos}'

    class Meta:
        db_table = 'Curso'
