from django.http import HttpResponse
from django.shortcuts import render,redirect

from Décés.forms import DecesForm
from Décés.models import Deces

# Create your views here
    #pour mariage

def Dece(request):  
    if request.method == "POST":  
        form = Form(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/showdécés')
            except:
                pass
    else:
        form=DecesForm()
    return render(request,'indexdécés.html',{'form':form})

def showdécés(request):  
    acte_décéss = Deces.objects.all()  
    return render(request,"showdécés.html",{'acte_décéss':acte_décéss})  


def editdécés(request,id):  
    acte_décéss = Deces.objects.get(id=id)  
    return render(request,"editdécés.html",{'acte_décés':acte_décés})

def update(request,id):
    acte_décés = Deces.objects.get(id=id)
    form = DecesForm(request.POST,instance=acte_décés)
    if form.is_valid():  
        form.save()
        return redirect('/showdécés')
    return render(request,"editdécés.html",{'acte_décés':acte_décés})

def destroy(request,id):
    acte_décés = Deces.objects.get(id=id)
    acte_décés.delete()
    return redirect('/showdécés')
