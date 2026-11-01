from django.contrib import admin

from .models import Categoria, Empleado, Servicio, Turno


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre"]


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "servicio", "categoria", "es_responsable", "usuario"]
    list_filter = ["servicio", "categoria", "es_responsable"]


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ["empleado", "fecha", "franja", "inicio", "fin"]
    list_filter = ["franja", "fecha"]
