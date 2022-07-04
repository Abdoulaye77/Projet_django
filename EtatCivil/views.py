from django.http import HttpResponse
from django.shortcuts import render,redirect

from EtatCivil.forms import MariageForm
from EtatCivil.models import Mariage

# Create your views here
    #pour mariage

def Mari(request):  
    if request.method == "POST":  
        form = MariageForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/showmariage')
            except:
                pass
    else:
        form=MariageForm()
    return render(request,'indexmariage.html',{'form':form})

def showmariage(request):  
    Actes_Mariages = Mariage.objects.all()  
    return render(request,"showmariage.html",{'Actes_Mariages':Actes_Mariages})  


def editmariage(request,id):  
    Actes_Mariages = Mariage.objects.get(id=id)  
    return render(request,"editmariage.html",{'Actes_Mariage':Actes_Mariage})

def update(request,id):
    Actes_Mariage = Mariage.objects.get(id=id)
    form = MariageForm(request.POST,instance=Actes_Mariage)
    if form.is_valid():  
        form.save()
        return redirect('/showmariage')
    return render(request,"editmariage.html",{'Actes_Mariage':Actes_Mariage})

def destroy(request,id):
    Actes_Mariage = Mariage.objects.get(id=id)
    Actes_Mariage.delete()
    return redirect('/showmariage')
