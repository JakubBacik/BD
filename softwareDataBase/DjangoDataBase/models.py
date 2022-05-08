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
