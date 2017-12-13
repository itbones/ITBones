from django.db import models
from datetime import date


# Create your nse models here.
class nse_m_stocklist(models.Model):
    stock_code = models.CharField(max_length=30)
    stock_desc = models.CharField(max_length=100,blank=True)
    buyprice = models.CharField(max_length=10,blank=True)
    buyqty = models.CharField(max_length=10,blank=True)
    buydate = models.DateField(null=True)
    notval1 = models.CharField(max_length=10,blank=True)
    notval2 = models.CharField(max_length=10,blank=True)
    notval3 = models.CharField(max_length=10,blank=True)
    buyvalue = models.CharField(max_length=10,blank=True)
    currprice = models.CharField(max_length=10,blank=True)
    currvalue = models.CharField(max_length=10,blank=True)
    realpos = models.CharField(max_length=10,blank=True)
    notes    = models.TextField(blank=True)
    stock_type = models.CharField(max_length=2,blank=True) # WL : Watchlist , SH : StockHeld , PL : PL Statement
    selldate = models.DateField(null=True)
    sellqty = models.CharField(max_length=10,blank=True)
    sellprice = models.CharField(max_length=10,blank=True)
    sellvalue = models.CharField(max_length=10,blank=True)
    plfinal = models.CharField(max_length=10,blank=True)
 
    def __str__(self):              # __unicode__ on Python 2
        return self.stock_code

    def holdingperiod(self):
        if self.selldate != '':
            return abs((self.selldate - self.buydate).days)
        else:
            return (1)

    def periodret(self):
        if self.selldate != '':
            zpl = float(self.sellvalue) - float(self.buyvalue)
            zdays = abs((self.selldate - self.buydate).days)
            zret = ((zpl * 100 * 365) / (float(self.buyvalue) * zdays))
            return round(zret,1)
        else:
            return (0) 
        
class nse_m_summarysheet(models.Model):
    stock_code = models.CharField(max_length=30)
    avgbuyprice = models.CharField(max_length=10,blank=True)
    totbuyqty = models.CharField(max_length=10,blank=True)
    totbuyvalue = models.CharField(max_length=10,blank=True)
    currprice = models.CharField(max_length=10,blank=True)
    currvalue = models.CharField(max_length=10,blank=True)
    realpos = models.CharField(max_length=10,blank=True)
    stock_type = models.CharField(max_length=2,blank=True) # WL : Watchlist , SH : StockHeld , PL : PL Statement

    def __str__(self):              # __unicode__ on Python 2
        return self.stock_code

class nse_m_stocknews(models.Model):
    stock_code = models.CharField(max_length=30)
    notedate = models.DateField(null=True,default=date.today)
    notes    = models.TextField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.stock_code
    