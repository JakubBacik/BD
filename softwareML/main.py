import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
import numpy as np

with open('Binance_BTCUSDT_minute.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    i=0
    j=0
    cost=0
    for row in spamreader:
        i+=1
        if i>2:
            some = row[6:7]
            float_lst = float(some[0])
            cost+=float_lst
            j+=1

            if j>4:
                time = row[1:2]
                print(time[0], cost/5)
                j=0
                cost=0


while True:
    page = requests.get(
        "https://www.google.com/finance/quote/BTC-PLN?sa=X&ved=2ahUKEwi_9--Imcb2AhUDyYsKHbETAbgQ-fUHegQIEhAS")
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.select('div.YMlKec.fxKbKc')[0].text.strip()
    time = soup.select('div.ygUjEc')[0].text.strip()
    print(time[0:19], price)
    sleep(300)




