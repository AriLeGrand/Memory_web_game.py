from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "profils/profil.html")

def leaderboard(request):
    return render(request, "profils/leaderboard.html")

