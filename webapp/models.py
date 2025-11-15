from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#007bff')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', '📝 Pendiente'),
        ('en_progreso', '🔄 En Progreso'),
        ('completada', '✅ Completada'),
    ]
    
    PRIORIDADES = [
        ('baja', '🟢 Baja'),
        ('media', '🟡 Media'),
        ('alta', '🔴 Alta'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
    def esta_vencida(self):
        if self.fecha_vencimiento and self.estado != 'completada':
            return self.fecha_vencimiento < timezone.now().date()
        return False
    
    class Meta:
        ordering = ['-fecha_creacion']