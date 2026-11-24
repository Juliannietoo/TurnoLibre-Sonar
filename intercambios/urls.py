from django.urls import path

from . import views

urlpatterns = [
    path("intercambios/proponer/<int:turno_id>/", views.proponer, name="proponer_intercambio"),
    path("intercambios/<int:pk>/", views.detalle, name="detalle_solicitud"),
    path(
        "intercambios/<int:pk>/responder/", views.responder, name="responder_solicitud"
    ),
]
