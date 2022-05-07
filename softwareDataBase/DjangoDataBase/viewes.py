from django.shortcuts import render
from .models import nowe
from .tasks import get_stock
import plotly.express as px

from django.shortcuts import render
import random
import datetime
import time

def show(request):
    '''
    dane = nowe.objects.all().values()
    return render(request, "database_list.html", {'danes': dane})
    '''
    dane = nowe.objects.all()

    fig = px.line(
        x = [c.date_time for c in dane],

        y = [c.price_low for c in dane],

    )

    chart = fig.to_html()

    context = {'chart': chart}
    return render(request, 'database_list.html', context)


