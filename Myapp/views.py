from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "Myapp/home.html")

def profil(request):
    return render(request, "Myapp/profil.html")
