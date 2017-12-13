from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from nsetools import Nse

from django.shortcuts import render
from .forms import nse_f_stocklist,nse_f_sellstock,nse_f_addwatchlititem,nse_f_stocknews
from .models import nse_m_stocklist , nse_m_summarysheet,nse_m_stocknews
import datetime
from .tables import *
from django_tables2 import RequestConfig

import smtplib

stock_list = nse_m_stocklist.objects.filter(stock_type = 'WL')     
for stock in stock_list:
        stockprice = 0
        nse = Nse()
        try:
                q = nse.get_quote(stock.stock_code)
                for price in q.items() :
                    if price[0] == 'lastPrice':
                        stockprice = price[1] 
                        break            
        except :
                stockprice = 0
        stock.currprice = stockprice
    #    stock.save()
        if (float(stock.currprice) < float(stock.notval1)) and (float(stock.currprice) > float(stock.notval3))  : # Buy more notification
            SUBJECT = 'Buy More Notification' + stock.stock_code + '\n'
            BODY =  stock.stock_code + ' stock has reached buy more notification \n' + stock.notval1
        if float(stock.currprice) > float(stock.notval2) : # Sell notification
            SUBJECT = 'Sell Notification' + stock.stock_code + '\n'
            BODY =  stock.stock_code + ' stock has reached Sell notification Levels \n' + stock.notval2  
        if float(stock.currprice) < float(stock.notval3) : # Stop Loss notification
            SUBJECT = 'Stop Loss Notification' + stock.stock_code + '\n'
            BODY =  stock.stock_code + ' stock has reached Stop Loss notification Levels \n' + stock.notval3    

        fromaddr = 'itbonessolutions@gmail.com'
        recipients = ['arokianathan.robert@outlook.com', 'arokianathan.robert@gmail.com']
        #toaddrs  = ", ".join(recipients)
        toaddrs = 'arokianathan.robert@outlook.com'
        #msg = 'Why,Oh why!'
        
        # Prepare actual message
        #msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
        #""" % (fromaddr, ", ".join(toaddrs), SUBJECT, BODY)
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, BODY)

        username = 'itbonessolutions@gmail.com'
        password = 'KuttyCatty@1'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg,)
        server.quit()     
 
