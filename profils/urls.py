from django.urls import path, include
from . import views

urlpatterns = [
    path("account", views.index, name="profils"),
    path("memory", include("memory.urls")),
]
