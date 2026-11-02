from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("entrar/", views.Entrar.as_view(), name="entrar"),
    path("salir/", LogoutView.as_view(), name="salir"),
    path("responsable/", views.panel_responsable, name="panel_responsable"),
]
