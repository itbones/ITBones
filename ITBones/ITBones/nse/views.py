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


# Create your nse views here.
def index(request):
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    stock_list = all_stock_codes.items()
  #  row = nse_m_stocklist()
  #  for stock in all_stock_codes.items():
  #      row.stock_code = stock[0]
   #     row.stock_desc = stock[1]
  #      row.save()
 #   stock_list = nse_m_stocklist.objects.order_by('-stock_code')
    return render(request, 'nse/index.html', {'table': stock_list})

def mystock(request,stockcode=None):
  if request.user.is_authenticated():
    investedtot = 0
    currentval = 0
    pltot = 0
    returnper = 0
    stock_news ={}
    
    if stockcode==None:
        stock_list = nse_m_stocklist.objects.filter(stock_type = 'SH')
    else:
        stock_list = nse_m_stocklist.objects.filter(stock_type = 'SH',stock_code = stockcode)

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
        stock.currvalue = round((float(stockprice) * float(stock.buyqty)),1)
        stock.buyvalue = round((float(stock.buyqty) * float(stock.buyprice)),1)  
        z = int(stock.currvalue) - int(stock.buyvalue)
        stock.realpos = ''
        stock.realpos = int(z)
        investedtot = investedtot + int(stock.buyvalue)
        currentval = currentval + int(stock.currvalue)
        pltot = pltot + stock.realpos # (currentval - investedtot)
        stock.save()
    try:
        returnper = int((pltot / investedtot) * 100)
    except:
        returnper = 0
    if stockcode==None:
        table_data = nse_m_stocklist.objects.filter(stock_type = 'SH')
        table_data = table_data.order_by('-stock_code')
        table = nse_t_stocklist(table_data)
        RequestConfig(request).configure(table)
    # Summary table
        summary_table = nse_t_summary([{'invval':investedtot,'curval':currentval,'retval':pltot,'retper':returnper}])
        RequestConfig(request).configure(summary_table)
        context = {'table': table,'table_sum':summary_table,}
        return render(request, 'nse/myallstock.html', context)
    else:
        table_data = nse_m_stocklist.objects.filter(stock_type = 'SH',stock_code = stockcode)
        table_data = table_data.order_by('-stock_code')
        table = nse_t_stocklist(table_data)
        RequestConfig(request).configure(table)
            # pass stock news
        stock_news = nse_m_stocknews.objects.filter(stock_code = stockcode)
        table_news = nse_t_stocknews(stock_news)
        RequestConfig(request).configure(table_news)
        
    # Summary table
        summary_table = nse_t_summary([{'invval':investedtot,'curval':currentval,'retval':pltot,'retper':returnper}])
        RequestConfig(request).configure(summary_table)
        context = {'table': table,'stock_news':table_news,'table_sum':summary_table,}
        return render(request, 'nse/mystock.html', context)
    
    
  else:
      return HttpResponseRedirect('/login')


def additem(request,stockcode=None):
    if request.method == "POST":
        # This is form class
        form = nse_f_stocklist(request.POST)
        form.valid = True
        stockprice = 0.
        if form.is_valid():
            post = form.save(commit=False)
            post.stock_type = 'SH'
            #post.user = 'system'
            #post.stamp = datetime.datetime.now()
            post.save()
            updatesummary(post,'buy')
            # Add data to summary table
          #  try:
          #      summary = nse_m_summarysheet.objects.get(stock_code = post.stock_code)
          #  except:
          #      summary = nse_m_summarysheet()
          ##  summary = nse_m_summarysheet.objects.filter(stock_type = 'SH')
          ##  summary_data = summary.filter(stock_code = post.stock_code)
          #  if not summary.id:
          #      summary_data = nse_m_summarysheet()
          #      summary_data.stock_code = post.stock_code
          #      summary_data.totbuyqty =  float(post.buyqty)
          #      summary_data.totbuyvalue =  float(post.buyqty) * float(post.buyprice)
          #      summary_data.avgbuyprice = float(post.buyprice)
          #      summary_data.stock_type = 'SH'
          #    #  summary_data.currprice = post.currprice
          #    #  summary_data.currvalue = float(post.currprice) * float(post.buyqty)
          #      summary_data.save()
          #  else:
          #      summary_data = nse_m_summarysheet(summary.id)
          #      summary_data.stock_code = post.stock_code
          #      summary_data.totbuyqty = float(summary.totbuyqty) + float(post.buyqty)
          #      summary_data.totbuyvalue = float(summary.totbuyvalue) + (float(post.buyqty) * float(post.buyprice)) 
          #      summary_data.avgbuyprice = float(summary.totbuyvalue) / float(summary.totbuyqty)
          #      summary_data.stock_type = 'SH'
          # #     summary_data.currprice = post.currprice
          # #     summary_data.currvalue = float(post.currprice) * float(summary_data.totbuyqty)
          #      summary_data.save()
        return redirect('Stock_Summary')
    else:
        form = nse_f_stocklist()
        nse = Nse()
        all_stock_codes = nse.get_stock_codes()
        stock_list = all_stock_codes.items()
        return render(request, 'nse/additem1.html', {'form': form , 'stock_list': stock_list })   
    
def maintainitem(request,stock_id):
    post = get_object_or_404(nse_m_stocklist, pk=stock_id)
    if request.method == "POST":
        form = nse_f_stocklist(request.POST, instance=post) 
        if form.is_valid():
            if 'delete_stock' in request.POST:
                # Stock Deleted
                post.delete()    
            elif 'change_stock' in request.POST: 
                # Stock Changes         
                form.save()
            return redirect('My_Stock_Listing_All')
    else:   
        try:
            form = nse_f_stocklist(instance=post)
            return render(request, 'nse/maintainitem.html', {'form': form})
        except Stock.DoesNotExist:
            raise Http404("Stock Code does not exist")
   # Render will render the page with the template but the url in the browser will be the same
   # Redirect will redirect to the required page and browser url will change    

def deletewatchlist(request,stock_id):
    post = nse_m_stocklist.objects.filter(id = stock_id)
    post.delete()
    return redirect('Watch_List')


def sellitem(request,stock_id,stockcode=None):
    post = get_object_or_404(nse_m_stocklist, pk=stock_id)
    if request.method == "POST":
        form = nse_f_sellstock(request.POST, instance=post) 
        if form.is_valid(): 
                post = form.save(commit=False)
                post.stock_type = 'PL'
                post.sellvalue = round((float(post.sellqty) * float(post.sellprice)),1) 
                post.plfinal = round((float(post.sellvalue) - float(post.buyvalue)),1)
                post.save()
                if post.sellqty < post.buyqty : # Partial sales save new record
                    post_new = nse_m_stocklist()
                    post_new.stock_type = 'SH'
                    post_new.stock_code = post.stock_code
                    post_new.buyprice = post.buyprice
                    post_new.buyqty = float(post.buyqty) - float(post.sellqty)
                    post_new.buydate = post.buydate
                    post_new.save()
                updatesummary(post,'sell')
        return redirect('My_Stock_Listing_All')
    else:   
        try:
            form = nse_f_sellstock(instance=post)
            return render(request, 'nse/sellitem.html', {'form': form})
        except Stock.DoesNotExist:
            raise Http404("Stock Code does not exist")


def plstatement(request):
    investedtot = 0
    currentval = 0
    pltot = 0
    returnper = 0
    stock_list = nse_m_stocklist.objects.filter(stock_type = 'PL')
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

        stock.buyvalue = round((float(stock.buyqty) * float(stock.buyprice)),1)  
        z = int(float(stock.sellvalue)) - int(stock.buyvalue)
        stock.realpos = ''
        stock.realpos = int(z)
        investedtot = investedtot + int(stock.buyvalue)
        currentval = currentval + int(float(stock.sellvalue))
        pltot = pltot + (currentval - investedtot)
        stock.save()
    try:
        returnper = int((pltot / investedtot) * 100)
    except:
        returnper = 0
    table_data = nse_m_stocklist.objects.filter(stock_type = 'PL')
    table = nse_t_pllist(table_data)
    RequestConfig(request).configure(table)

     # Summary table
    summary_table = nse_t_summary([{'invval':investedtot,'curval':currentval,'retval':pltot,'retper':returnper}])
    RequestConfig(request).configure(summary_table)
    context = {'table': table,'table_sum':summary_table,}
   
    return render(request, 'nse/plstatement.html', context)

def watchlist(request):
    investedtot = 0
    currentval = 0
    pltot = 0
    returnper = 0
    #stock_list = nse_m_stocklist.objects.exclude(stock_type = 'PL')
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
        stock.save()
    
   # table_data = nse_m_stocklist.objects.exclude(stock_type = 'PL')
    table_data = nse_m_stocklist.objects.filter(stock_type = 'WL')
    table = nse_t_watchlist(table_data)
    RequestConfig(request).configure(table)
    context = {'table': table}
    return render(request, 'nse/watchlist.html', context)

def addwatchlistitem(request):
    if request.method == "POST":
        # This is form class
        form = nse_f_addwatchlititem(request.POST)
        form.valid = True
        if form.is_valid():
            post = form.save(commit=False)
            post.stock_type = 'WL'
            #post.user = 'system'
            #post.stamp = datetime.datetime.now()
            post.save()
        return redirect('Watch_List')
    else:
        form = nse_f_addwatchlititem()
        nse = Nse()
        all_stock_codes = nse.get_stock_codes()
        stock_list = all_stock_codes.items()
        return render(request, 'nse/addwatchlistitem.html', {'form': form , 'stock_list': stock_list })   

def sendemail(request):
    # check for breakeven price
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
  
     return redirect('My_Stock_Summary')

def summarysheet(request):
  if request.user.is_authenticated():
    investedtot = 0
    currentval = 0
    pltot = 0
    returnper = 0

    stock_list = nse_m_summarysheet.objects.filter(stock_type = 'SH')
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
        stock.currvalue = round((float(stockprice) * float(stock.totbuyqty)),1)
        stock.buyvalue = round((float(stock.totbuyqty) * float(stock.avgbuyprice)),1)  
        z = int(stock.currvalue) - int(stock.buyvalue)
        stock.realpos = ''
        stock.realpos = int(z)
        investedtot = investedtot + int(stock.buyvalue)
        currentval = currentval + int(stock.currvalue)
        pltot = pltot + stock.realpos # (currentval - investedtot)
        stock.save()
    try:
        returnper = int((pltot / investedtot) * 100)
    except:
        returnper = 0
    table_data = nse_m_summarysheet.objects.filter(stock_type = 'SH')
    table_data = table_data.order_by('-stock_code')
    table = nse_t_summarysheet(table_data)
    RequestConfig(request).configure(table)

     # Summary table
    summary_table = nse_t_summary([{'invval':investedtot,'curval':currentval,'retval':pltot,'retper':returnper}])
    RequestConfig(request).configure(summary_table)

    context = {'table': table,'table_sum':summary_table,}
    return render(request, 'nse/summarysheet.html', context)
  else:
      return HttpResponseRedirect('/login')


# Stock News Modules

def addstocknews(request,stockcode):
    if request.method == "POST":
        # This is form class
        form = nse_f_stocknews(request.POST)
        form.valid = True
        if form.is_valid():
            form.save()
        return redirect('Stock_Summary')
    else:
        form = nse_f_stocknews(initial={'stock_code': stockcode})
       # nse = Nse()
      #  all_stock_codes = nse.get_stock_codes()
      #  stock_list = all_stock_codes.items()
      #  form.stock_code = stockcode
        return render(request, 'nse/addstocknews.html', {'form': form  })

def updatesummary(post,trans):
            try:
                summary = nse_m_summarysheet.objects.get(stock_code = post.stock_code)
            except:
                summary = nse_m_summarysheet()
            if  summary.id and trans=='sell' :
                summary_data = nse_m_summarysheet(summary.id)
                summary_data.stock_code = post.stock_code
                summary_data.totbuyqty = float(summary.totbuyqty) - float(post.sellqty)
                summary_data.totbuyvalue = float(summary.totbuyvalue) - (float(post.sellqty) * float(post.buyprice)) 
                if float(summary_data.totbuyqty) == 0:
                   summary_data.avgbuyprice = 0
                else:
                    summary_data.avgbuyprice = float(summary_data.totbuyvalue) / float(summary_data.totbuyqty)
                summary_data.stock_type = 'SH'
           #     summary_data.currprice = post.currprice
           #     summary_data.currvalue = float(post.currprice) * float(summary_data.totbuyqty)
                summary_data.save()
            elif summary.id and trans=='buy' :
                summary_data = nse_m_summarysheet(summary.id)
                summary_data.stock_code = post.stock_code
                summary_data.totbuyqty = float(summary.totbuyqty) + float(post.buyqty)
                summary_data.totbuyvalue = float(summary.totbuyvalue) + (float(post.buyqty) * float(post.buyprice)) 
                summary_data.avgbuyprice = float(summary_data.totbuyvalue) / float(summary_data.totbuyqty)
                summary_data.stock_type = 'SH'
                summary_data.save()
            else:
                summary_data = nse_m_summarysheet()
                summary_data.stock_code = post.stock_code
                summary_data.totbuyqty =  float(post.buyqty)
                summary_data.totbuyvalue =  float(post.buyqty) * float(post.buyprice)
                summary_data.avgbuyprice = float(post.buyprice)
                summary_data.stock_type = 'SH'
                summary_data.save()
            if int(summary_data.totbuyqty) == 0:
                summary_data = nse_m_summarysheet(summary.id)
                summary_data.delete()

            return;
