from background_task import background
from DjangoDataBase.models import dane_po_predykcji
from DjangoDataBase.models import pobrane_dane
from DjangoDataBase.models import dane_do_wyswietlenia
import DjangoDataBase.models
from DjangoDataBase.models import nowe
import yfinance as yf
import random
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
import numpy as np
import time
from threading import Timer
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import tensorflow as tf
import numpy as np
from DjangoDataBase.main import scale_test_data, inverse_scaler, pred_length, get_data, scale_train_data
import matplotlib.pyplot as plt

def schedulTask():
    current_data()
    scaled_predictions, predictions_list = make_predictions()
    data_after_prediction(scaled_predictions)
    data_after_prediction1(predictions_list)
    #exec(open("DjangoDataBase/future_predictions.py").read())



def current_data():
    data = yf.download(tickers='BTC-USD', period='5m', interval='5m')
    dataTime = data.index
    value_close = data['Close'].to_numpy()[0]
    value_open = data['Open'].to_numpy()[0]

    currentNumber = pobrane_dane.objects.count()
    new_entry = pobrane_dane(id_pobrane_dane=currentNumber+1, data_pobrania=dataTime[0],  wartosc_open= value_open, wartosc_close = value_close, symbol= 'USD')
    new_entry.save()



def insert_data_from_csv():
    data = yf.download(tickers='BTC-USD', period='5h', interval='5m')
    dataTime = data.index
    value_close = data['Close'].to_numpy()
    value_open = data['Open'].to_numpy()

    for i in range(0, len(value_open)-1):
        new_entry = pobrane_dane(id_pobrane_dane= i+1, data_pobrania=dataTime[i], wartosc_open=value_open[i], wartosc_close=value_close[i], symbol='USD')
        new_entry.save()

def data_after_prediction(data):
    start = roundTime(datetime.now()- timedelta(hours=2), roundTo=4*60)
    end = start + timedelta(hours=1)
    min_gap = 5
    currentNumber = pobrane_dane.objects.count()
    k=0
    dane_po_predykcji.objects.filter(id_danych_po_predykcji=pobrane_dane.objects.count()).delete()
    for i in range(int((end - start).total_seconds() / 60.0 / min_gap)):
        array = ((start + timedelta(hours=min_gap * i / 60)))
        new_entry = dane_po_predykcji(id_danych_po_predykcji= currentNumber+1, data_pobrania=array, przeskalowana_wartosc_ceny = data[k])
        currentNumber+=1
        k+=1
        new_entry.save()


def data_after_prediction1(data):
    currenNumber1 = 12 + pobrane_dane.objects.count()
    i=0
    dane_do_wyswietlenia.objects.filter(id_dane_do_wyswietlenia=pobrane_dane.objects.count()).delete()
    for k in range(pobrane_dane.objects.count()+1, currenNumber1+1):
        obj = dane_do_wyswietlenia.objects.get(id_dane_do_wyswietlenia= k)
        obj.cena = data[i]
        i+=1
        obj.save()

def deleteData():
    currenNumber12 = pobrane_dane.objects.count()
    currenNumber1 = dane_do_wyswietlenia.objects.count()
    for k in range(currenNumber12, currenNumber12 + currenNumber1+1):
        dane_po_predykcji.objects.filter(id_danych_po_predykcji = k).delete()

def deleteData1():
    currenNumber1 = dane_do_wyswietlenia.objects.count()
    for k in range(pobrane_dane.objects.count()+1, currenNumber1+1):
        obj = dane_do_wyswietlenia.objects.filter(id_dane_do_wyswietlenia = k).delete()


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def roundTime(dt=None, roundTo=60):
   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

def make_predictions():
    test = scale_test_data()
    test = test.reshape(len(test), len(test[0]), 1)
    model = tf.keras.models.load_model('DjangoDataBase/saved_model/Model_8')

    scaled_predictions, predictions_list = [], []

    for i in range(0, pred_length):
        y_pred = model.predict(test)
        scaled_predictions.append(y_pred[0, -1][0])
        test = np.concatenate((test[0], [y_pred[0, -1]]), axis=0)
        test = np.delete(test, 0, axis=0)
        test = test.reshape(1, len(test), 1)

    print(scaled_predictions)
    predictions_list = inverse_scaler(np.array(scaled_predictions).reshape(1,-1)).flatten().tolist()
    print(predictions_list)

    return scaled_predictions, predictions_list


