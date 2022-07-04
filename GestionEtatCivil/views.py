from datetime import datetime

from django.shortcuts import render


def Acceuil(request):
    return render(request, "Acceuil.html", context={"date": datetime.today()})
def home(request):
    return render(request, 'home.html')
def indexmairie(request):
    return render(request, 'indexmairie.html')
def indexmariage(request):
    return render(request, 'indexmariage.html')
def indexnaissance(request):
    return render(request, 'indexnaissance.html')