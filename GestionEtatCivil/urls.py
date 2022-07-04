"""GestionEtatCivil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import Acceuil,home,indexmariage,indexnaissance,indexmairie
from Utilisateur.views import login , creer_compt



urlpatterns = [
    path('', Acceuil, name="Acceuil"),
    path('', indexmairie, name="indexmairie"),
    path('', indexmariage, name="indexmariage"),
    path('', indexnaissance, name="indexnaissance"),
    path('creer_compt',creer_compt, name="creer_compt"),
    path('login/',login, name="login"),
    
    path('admin/', admin.site.urls),

    path('EtatCivil/', include('EtatCivil.urls')),
    path('EtatcivilNaiss/', include('EtatcivilNaiss.urls')),
    path('Mairie/', include('Mairie.urls')),
    path('Décés/', include('Décés.urls')),

    path('Mari/', include('EtatCivil.urls')),
    path('mair/', include('Mairie.urls')),
    path('Naiss/', include('EtatcivilNaiss.urls')),
    path('Dece/', include('Décés.urls')),
    
    path('showmariage/', include('EtatCivil.urls')),
    path('showmairie/', include('Mairie.urls')),
    path('shownaissance/', include('EtatcivilNaiss.urls')),
     path('showdécés/', include('Décés.urls')),
    

]
