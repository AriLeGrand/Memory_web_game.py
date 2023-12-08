from django.shortcuts import render
from profils.models import Leaderboard, HistoricalScore


# Create your views here.
def index(request):
    return render(request,'memory\\memory.html')

def ParseGameResults(request):
    Leaderboard(user=request.user, score=request.POST.get("totalPoints", None)).save()
    HistoricalScore(user=request.user, score=request.POST.get("totalPoints", None)).save()
    return render(request,'memory\\memory.html')
    