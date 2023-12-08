from django.db import models
from django.contrib.auth.models import User

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    
class HistoricalScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)