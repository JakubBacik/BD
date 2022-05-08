from background_task import background
from DjangoDataBase.models import nowe
import yfinance as yf
import random



#@background(schedule=5)
def get_stock():
     i = 0
     for n in range(1,24):
          for k in range(1,60):
               dt = "2022-08-25 " + str(n) + ":" + str(k) + ":" + "00"
               low = i
               high = i
               new_entry = nowe(date_time=dt, price_low=low, price_high=high)
               new_entry.save()
               i+=1




