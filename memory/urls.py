from django.urls import path, include
from . import views

urlpatterns = [
    path("memory", views.index, name="memory"),
]


