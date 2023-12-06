from django.urls import path, include
from . import views

urlpatterns = [
    path("memory", views.index, name="memory"),
    path("", include("Myapp.urls")),
    path("profils", include("profils.urls")),
    path("LLR", include("LLR.urls")),
]


