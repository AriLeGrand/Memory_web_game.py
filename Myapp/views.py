from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def profil(request):
    return render(request, "profil.html")
