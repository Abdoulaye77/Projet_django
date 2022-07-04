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
from django.conf import settings
from .views import redirect_view
from django.conf.urls.static import static 
from EtatcivilNaiss import views
from EtatcivilNaiss import models
from EtatcivilNaiss import forms
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin', admin.site.urls),
    path("login",views.login, name='login'),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    path("entrylogin", views.entrylogin, name="entry"),
    path("searchtable1",views.searchtable1, name="entry"),
    path("searchtable2",views.searchtable2, name="entry"),
    path("searchtable3",views.searchtable3, name="entry"),
    path("searchtable4",views.searchtable4, name="entry"),
    #path("filters",views.filters, name="filters"),
    path("ourusers",views.ourusers, name="entry"),
    path("entrysignup", views.entrysignup, name="entry"),
    path("searchin",views.searchin,name="searchin"),
    #path("profile",views.profile,name="profile"),
    path("profile/<str:pk_test>",views.profile, name="profile"),
    path("update/<str:pk>",views.update, name="update"),
    path("delete/<str:pk2>",views.delete, name="delete"),
    
    #path("d",views.d, name='d')
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)