from django.urls import path
from . import views

urlpatterns = [
    path("memory", views.index, name="memory"),
]
