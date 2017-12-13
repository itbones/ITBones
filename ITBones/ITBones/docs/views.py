from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from nsetools import Nse

from django.shortcuts import render
from .forms import doc_f_docmaster
from .models import doc_m_docmaster
import datetime
from .tables import doc_t_docmaster
from django_tables2 import RequestConfig

import smtplib

# Create your docs views here.

def adddoc(request):
    if request.method == "POST":
        # This is form class
        form = doc_f_docmaster(request.POST)
        form.valid = True
        if form.is_valid():
            post = form.save(commit=False)
            post.stock_type = 'SH'
            post.save()
        return redirect('Doc_List')
    else:
        form = doc_f_docmaster()
        return render(request, 'docs/adddoc.html', {'form': form }) 
    
def doclist(request):
    doc_list = doc_m_docmaster.objects.order_by('-doc_area')
    table = doc_t_docmaster(doc_list)
    RequestConfig(request).configure(table)
    return render(request, 'docs/doclist.html', {'table': table})

def displaydoc(request,doc_id):
    post = get_object_or_404(doc_m_docmaster, pk=doc_id) 
    try:
       form = doc_f_docmaster(instance=post)
       return render(request, 'docs/displaydoc.html', {'form': post})
    except Stock.DoesNotExist:
       raise Http404("Document not exist")

def changedoc(request,doc_id):
    post = get_object_or_404(doc_m_docmaster, pk=doc_id)
    if request.method == "POST":
        form = doc_f_docmaster(request.POST, instance=post) 
        if form.is_valid():
            if 'delete_stock' in request.POST:
                # Stock Deleted
                post.delete()    
            elif 'change_stock' in request.POST: 
                # Stock Changes         
                form.save()
            return redirect('Doc_List')
    else:   
        try:
            form = doc_f_docmaster(instance=post)
            return render(request, 'docs/changedoc.html', {'form': form})
        except Stock.DoesNotExist:
            raise Http404("Document doesnt exist")


