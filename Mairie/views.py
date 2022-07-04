from django.shortcuts import render
from .models import Mairie





# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect

from Mairie.forms import MairieForm
from Mairie.models import Mairie

# Create your views here

def mair(request):  
    if request.method == "POST":  
        form = MairieForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/showmairie')
            except:
                pass
    else:
        form=MairieForm()
    return render(request,'indexmairie.html',{'form':form})

def showmairie(request):  
    str_mairies = Mairie.objects.all()  
    return render(request,"showmairie.html",{'str_mairies':str_mairies})    


def editmairie(request,id):  
    str_mairie = Mairie.objects.get(id=id)  
    return render(request,"editmairie.html",{'str_mairie':str_mairie})

def update(request,id):
    str_mairie = Mairie.objects.get(id=id)
    form = MairieForm(request.POST,instance=str_mairie)
    if form.is_valid():  
        form.save()
        return redirect('/showmairie')
    return render(request,"editmairie.html",{'str_mairie':str_mairie})

def destroy(request,id):
    str_mairie = Mairie.objects.get(id=id)
    str_mairie.delete()
    return redirect('/showmairie')


# Create your views here.
