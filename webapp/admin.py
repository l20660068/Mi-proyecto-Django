from django.contrib import admin
from .models import Tarea, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color']
    search_fields = ['nombre']

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'estado', 'prioridad', 'categoria', 'fecha_creacion']
    list_filter = ['estado', 'prioridad', 'categoria', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']