from django.urls import path

from . import views

urlpatterns = [
    path("calendario/", views.calendario, name="calendario"),
    path("compatibles/", views.compatibles, name="compatibles"),
]
