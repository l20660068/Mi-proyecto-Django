from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Tarea, Categoria
from .forms import TareaForm, CategoriaForm

def dashboard(request):
    tareas = Tarea.objects.all()
    
    # Estadísticas
    total_tareas = tareas.count()
    tareas_completadas = tareas.filter(estado='completada').count()
    tareas_pendientes = tareas.filter(estado='pendiente').count()
    tareas_vencidas = len([t for t in tareas if t.esta_vencida()])
    
    # Filtros
    estado = request.GET.get('estado')
    prioridad = request.GET.get('prioridad')
    categoria = request.GET.get('categoria')
    
    if estado:
        tareas = tareas.filter(estado=estado)
    if prioridad:
        tareas = tareas.filter(prioridad=prioridad)
    if categoria:
        tareas = tareas.filter(categoria_id=categoria)
    
    categorias = Categoria.objects.all()
    
    context = {
        'tareas': tareas,
        'form_tarea': TareaForm(),
        'form_categoria': CategoriaForm(),
        'categorias': categorias,
        'estadisticas': {
            'total': total_tareas,
            'completadas': tareas_completadas,
            'pendientes': tareas_pendientes,
            'vencidas': tareas_vencidas,
        }
    }
    return render(request, 'webapp/dashboard.html', context)

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Tarea creada exitosamente!')
            return redirect('dashboard')
    
    return redirect('dashboard')

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '📂 Categoría creada exitosamente!')
            return redirect('dashboard')
    
    return redirect('dashboard')

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Tarea actualizada!')
            return redirect('dashboard')
    
    # Para GET, mostramos el formulario en modal
    form = TareaForm(instance=tarea)
    tareas = Tarea.objects.all()
    categorias = Categoria.objects.all()
    
    return render(request, 'webapp/dashboard.html', {
        'tareas': tareas,
        'form_tarea': form,
        'form_categoria': CategoriaForm(),
        'categorias': categorias,
        'tarea_editar': tarea
    })

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, '🗑️ Tarea eliminada!')
    return redirect('dashboard')

def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['pendiente', 'en_progreso', 'completada']:
            tarea.estado = nuevo_estado
            tarea.save()
            messages.success(request, f'Estado actualizado!')
    
    return redirect('dashboard')