from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("profil/", views.profil, name="profil"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("register", views.register, name="register"),
    path('admin', admin.site.urls),
    path("profils", include("profils.urls")),
    path("memory", include("memory.urls")),
    path("LLR", include("LLR.urls")),
]
