from django.shortcuts import render
from .models import Leaderboard, HistoricalScore
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "profils/profil.html")

def leaderboard(request):
    leaderboard_data = Leaderboard.objects.order_by('-score', 'time')[:10]
    return render(request, 'profils/leaderboard.html', {'leaderboard_data': leaderboard_data})

def historical_score(request):
    historical_score_data = HistoricalScore.objects.order_by('-score', 'time')[:10]
    return render(request, 'profils/historical_score.html', {'historical_score_data': historical_score_data})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return render(request, 'leaderboard.html',)