from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from django.shortcuts import render
from .forms import *
from .models import m_webmark
import datetime
from .tables import *
from django_tables2 import RequestConfig


# Create your views here.
def index(request):
    webmark_list = m_webmark.objects.order_by('-topic')
   # context = {'webmark_list': webmark_list}
   # return render(request, 'webmark/index.html', context)
    table = t_webmark(webmark_list)
    RequestConfig(request).configure(table)
    return render(request, 'webmark/index.html', {'table': table})


def addwebmark(request):
    if request.method == "POST":
        # This is form class
        form = f_webmark(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = 'system'
            post.stamp = datetime.datetime.now()
            post.save()
        return redirect('index')
    else:
        form = f_webmark()
        return render(request, 'webmark/add_webmark.html', {'form': form})    