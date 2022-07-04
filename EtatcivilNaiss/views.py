
from django.shortcuts import render, HttpResponse, redirect
from EtatcivilNaiss.models import Naissance
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from EtatcivilNaiss.forms import NaissanceForm
from django.core.files import File

from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')

def login(request):
    count = Naissance.objects.all().count()
    context = {'count':count}
    return render(request, 'login.html', context)
 
def redirect_view(request):
    response = redirect('/login/')
    return response

def entrylogin(request):
    
    if request.method == 'POST':
        try:
            uname = request.POST["uname"]
            psw = request.POST["psw"]
            for custom_users in Naissance.objects.all():
                if str(custom_users.uname) == uname:
                    login_obj = custom_users
                    break
                else:
                    login_obj = None

            if login_obj is not None:
                if str(login_obj.psw) == psw:
                    request.session['session'] = uname
                    return redirect('/login')
                    #return render(request, 'login.html', {'display' : data})
                else:
                    return redirect('/')
            else:
                return redirect('/')
        except:
            return HttpResponse("exception... !!")

def ourusers(request):
    data=Naissance.objects.all()
    count=data.count()
    context = {'display':data, 'count':count}
    return render(request, 'login.html', context)

def profile(request, pk_test):
    user=Naissance.objects.get(uname=pk_test)
    return render(request, 'profile.html', {'userprofile' : user})

def update(request, pk):
    user=Naissance.objects.get(uname=pk)
    form=Naissance(instance=user)
    if request.method == 'POST':
        form = NaissanceForm(request.POST, instance=user) 
        if form.is_valid(): 
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update.html', context)

def delete(request, pk2):
    user=Naissance.objects.get(uname=pk2)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    context = {'user': user}
    return render(request, 'delete.html', context)

def entrysignup(request):
    if request.method == 'POST' or request.FILES == 'file':
        #fname=request.POST["fname"]
        form = NaissanceForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = NaissanceForm() 
    return render(request, 'EtatcivilNaiss/index.html',{'form':form}) 

def searchin(request):
    return render(request, 'searchin.html')


def searchtable1(request):
    if request.method == 'POST':
        u = request.POST["u"]
    s=Naissance.objects.filter(fname=u)
    context = {'set':s}
    return render(request, 'searchin.html', context)

def searchtable2(request):
    
    if request.method == 'POST':
        c = request.POST["c"]
    s=Naissance.objects.filter(city=c)
    return render(request, 'searchin.html', {'set1' : s})


def searchtable3(request):
    if request.method == 'POST':
        g = request.POST["g"]
    s=Naissance.objects.filter(gender=g)
    return render(request, 'searchin.html', {'set2' : s})

def searchtable4(request):
    if request.method == 'POST':
        m = request.POST["m"]
    s=Naissance.objects.filter(marital_status=m)
    return render(request, 'searchin.html', {'set3' : s})