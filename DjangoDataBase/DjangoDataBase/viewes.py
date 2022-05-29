from django.shortcuts import render
import DjangoDataBase.models
from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.express as px

def showChart(request):
    '''
    dane = nowe.objects.all().values()
    return render(request, "database_list.html", {'danes': dane})
    '''
    dane = DjangoDataBase.models.dane_do_wyswietlenia.objects.all().order_by("id_dane_do_wyswietlenia")
    dane2 = DjangoDataBase.models.pobrane_dane.objects.all().order_by("id_pobrane_dane")
    predykcja = []
    aktualne = [k.wartosc_close for k in dane2]
    k = [c.data_pobrania for c in dane2]
    for c in dane:
        k.append(c.id_danych_po_predykcji.data_pobrania)
        aktualne.append('')

    for i in range(0, dane2.count()):
        predykcja.append('')

    for c in dane:
        predykcja.append(c.cena)


    value = {'predykcja': predykcja, 'aktualne': aktualne}
    print(len(value['predykcja']), len(value['aktualne']), len(k))


    df = pd.DataFrame(data = value)
    fig = px.line(df,
        x= k,
        y= ['predykcja', 'aktualne'],
        title="Wykres predykcji ceny", labels={'x': 'Czas', 'value': 'USD'}
    )

    fig.update_layout(
        template = "plotly_white"
    )

    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, 'database_list.html', context)

def showDataPobraneDane(request):
    pobraneDane = DjangoDataBase.models.pobrane_dane.objects.all().values()
    return render(request, "PobraneDane.html", {'pobraneDane': pobraneDane })

def showDataDaneDoPredykcji(request):
    daneDoPredykcji = DjangoDataBase.models.dane_do_predykcji.objects.all().values()
    return render(request, "DaneDoPredykcji.html", {'daneDoPredykcji':daneDoPredykcji})

def showDataDanePoPredykcji(request):
    danePoPredykcji = DjangoDataBase.models.dane_po_predykcji.objects.all().values().order_by("id_danych_po_predykcji")
    return render(request, "DanePoPredykcji.html", {'danePoPredykcji':danePoPredykcji})

def showDataDaneDoWyswietlenia(request):
    daneDoWyswietlenia = DjangoDataBase.models.dane_do_wyswietlenia.objects.all().values().order_by("id_dane_do_wyswietlenia")
    return render(request, "DaneDoWyswietlenia.html", {'daneDoWyswietlenia':daneDoWyswietlenia })

def home(request):
    return render(request, "home.html")