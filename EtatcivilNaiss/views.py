

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect

from EtatcivilNaiss.forms import NaissanceForm
from EtatcivilNaiss.models import Naissance

# Create your views here

def Naiss(request):  
    if request.method == "POST":  
        form = NaissanceForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/shownaissance')
            except:
                pass
    else:
        form=NaissanceForm()
    return render(request,'indexnaissance.html',{'form':form})

def shownaissance(request):  
    Actes_Naissances = Naissance.objects.all()  
    return render(request,"shownaissance.html",{'Actes_Naissances':Actes_Naissances})    


def editnaissance(request,id):  
    Actes_Naissance = Naissance.objects.get(id=id)  
    return render(request,"editnaissance.html",{'Actes_Naissance':Actes_Naissance})

def update(request,id):
    Actes_Naissance = Naissance.objects.get(id=id)
    form = NaissanceForm(request.POST,instance=Actes_Naissance)
    if form.is_valid():  
        form.save()
        return redirect('/shownaissance')
    return render(request,"editnaissance.html",{'Actes_Naissance':Actes_Naissance})

def destroy(request,id):
    Actes_Naissance = Naissance.objects.get(id=id)
    Actes_Naissance.delete()
    return redirect('/shownaissance')
