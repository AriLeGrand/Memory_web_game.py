from django.urls import path, include
from . import views

urlpatterns = [
    path("memory", views.index, name="memory"),
    path("memory/ParseGameResults", views.ParseGameResults, name="ParseGameResults"),
]


