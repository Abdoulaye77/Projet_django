from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
#from django.contrib.auth import  get_user_model

#User = get_user_model()

def login(request):
    return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('Acceuil')
def creer_compt(request):
    return render(request, 'creer_compt.html')