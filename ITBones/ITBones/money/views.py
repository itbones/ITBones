
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from .models import Stock
from .forms import *


def index(request):
    stock_list = Stock.objects.order_by('-stock_code')
    context = {'stock_list': stock_list}
    return render(request, 'money/index.html', context)

def addstock(request):
    if request.method == "POST":
        # This is form class
        form = PostStock(request.POST) 
        if form.is_valid():
           # post = form.save(commit=False)
          #  post.author = request.user
          #  post.published_date = timezone.now()
            form.save()
           # return redirect('post_detail', pk=post.pk)
          
           # Return to index page after refresh
          #  stock_list = Stock.objects.order_by('-stock_code')
          #  context = {'stock_list': stock_list}
          #  return render(request, 'money/index.html', context)
        return redirect('index')
    else:
        form = PostStock()
        return render(request, 'money/addstock.html', {'form': form})

def displaystock_v(request,stockid):
    post = get_object_or_404(Stock, pk=stockid)
    if request.method == "POST":
        form = PostStock(request.POST, instance=post) 
        if form.is_valid():
            form.save()
         #   stock_list = Stock.objects.order_by('-stock_code')
         #   context = {'stock_list': stock_list}
            return redirect('index')
         #   return redirect('money/index.html')
         #   return render(request, 'money/index.html', context)
    else:   
        try:
          #  stock = Stock.objects.get(pk=stockid)
        # stock = get_object_or_404(Stock, pk=stockid)
            form = PostStock(instance=post)
            return render(request, 'money/display_stock.html', {'form': form})
        except Stock.DoesNotExist:
            raise Http404("Stock Code does not exist")
   # Render will render the page with the template but the url in the browser will be the same
   # Redirect will redirect to the required page and browser url will change     



def sendemail(request):

      send_mail('This is a test mail',
               'Please be noted this is being sent from me',
              'itbonessolutions@gmail.com', 
              ['arokianathan.robert@outlook.com'],
             fail_silently=False)
      messages.add_message(request, messages.INFO, 'Email sent')
      return redirect('index')