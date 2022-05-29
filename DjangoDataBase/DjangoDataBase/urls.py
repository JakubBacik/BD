"""DjangoDataBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from DjangoDataBase import viewes
from .viewes import showChart
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', viewes.home, name='home'),
    path('DaneDoPredykcji', viewes.showDataDaneDoPredykcji, name='DaneDoPredykcji'),
    path('DaneDoWyswietlenia', viewes.showDataDaneDoWyswietlenia, name='DaneDoWyswietlenia'),
    path('DanePoPredykcji', viewes.showDataDanePoPredykcji, name='DanePoPredykcji'),
    path('PobraneDane', viewes.showDataPobraneDane, name='PobraneDane'),
    path('Wykres', viewes.showChart, name='chart'),
]
urlpatterns += staticfiles_urlpatterns()