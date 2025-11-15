from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('crear-tarea/', views.crear_tarea, name='crear_tarea'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('editar-tarea/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar-tarea/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('cambiar-estado/<int:tarea_id>/', views.cambiar_estado, name='cambiar_estado'),
]