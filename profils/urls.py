from django.urls import path, include
from . import views

urlpatterns = [
    path("account", views.index, name="profils"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("", views.logout_view, name="logout"),
]
