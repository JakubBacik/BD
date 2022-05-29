from django.db import models

class nowe(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    price_low = models.FloatField()
    price_high = models.FloatField()

    class Meta:
        db_table = 'DBAPP_STOCKS'
        required_db_vendor = 'oracle'
'''
    def __unicode__(self):
        return  self.datetime + ' ' + self.price_low + ' ' + self.price_high
'''

class pobrane_dane(models.Model):
    id_pobrane_dane = models.IntegerField(primary_key=True)
    data_pobrania = models.DateTimeField()
    wartosc_open = models.FloatField()
    wartosc_close = models.FloatField()
    symbol = models.CharField(max_length=8)

    class Meta:
        db_table = 'POBRANE_DANE'
        required_db_vendor = 'oracle'


class dane_do_predykcji(models.Model):
    id_dane_do_predykcji = models.IntegerField(primary_key=True)
    przeskalowana_wartosc_ceny = models.FloatField()
    id_pobrane_dane = models.ForeignKey(pobrane_dane, on_delete=models.CASCADE)

    class Meta:
        db_table = 'DANE_DO_PREDYKCJI'
        required_db_vendor = 'oracle'


class dane_po_predykcji(models.Model):
    id_danych_po_predykcji = models.IntegerField(primary_key=True)
    data_pobrania = models.DateTimeField()
    przeskalowana_wartosc_ceny = models.FloatField()

    class Meta:
        db_table = 'DANE_PO_PREDYKCJI'
        required_db_vendor = 'oracle'


class dane_do_wyswietlenia(models.Model):
    id_dane_do_wyswietlenia = models.IntegerField(primary_key=True)
    cena = models.FloatField()
    id_danych_po_predykcji = models.ForeignKey(dane_po_predykcji, on_delete=models.CASCADE)

    class Meta:
        db_table = 'DANE_DO_WYSWIETLENIA'
        required_db_vendor = 'oracle'
