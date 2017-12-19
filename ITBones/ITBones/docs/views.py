from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse,HttpRequest
from django.contrib import messages
from datetime import datetime

from django.shortcuts import render
from .forms import doc_f_docmaster,doc_f_files
from .models import doc_m_docmaster,doc_m_files
import datetime
from .tables import doc_t_docmaster,doc_t_files
from django_tables2 import RequestConfig

import smtplib

# Create your docs views here.
def index(request):
    search = ''
    try: 
        search = request.GET['search']
        result = doc_m_docmaster.objects.filter(doc_sub__icontains=search)
        
    except:
        result = {}
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'docs/index.html',
        {
            'title':'Home Page',
            'result': result,
             'search' : search,
        }
    )



def adddoc(request):
    if request.method == "POST":
        # This is form class
        form = doc_f_docmaster(request.POST,request.FILES)
        form.valid = True
        if form.is_valid():
            try:
                fileupload = doc_m_files(file_data_public=request.FILES['file_data_private'])
                fileupload = populatefile_db(fileupload)
            except:
                fileupload = None

            if 'add_doc' in request.POST:
                post = form.save(commit=False)
                post.stock_type = 'SH'
                post.save()
            elif 'upload_public' in request.POST: 
                fileupload.file_name = fileupload.file_data_public.name
                fileupload.save()
              # Formatting google drive string
                str1 =  fileupload.file_data_public.url
                str2 = str1.replace("https://drive.google.com/file/d/","https://docs.google.com/uc?id=")
                str3 = str2.replace("/view?usp=drivesdk","")
              #  form = doc_f_docmaster(instance=form)
              #  form.file_name = fileupload.file_data
                docupload = doc_f_files()
                return render(request, 'docs/adddoc.html', {'form': form , 'file' : docupload , 'attlink':str3  })
            elif 'upload_private' in request.POST: 
                fileupload.file_name = fileupload.file_data_public.name
                fileupload.file_data_private = fileupload.file_data_public
                fileupload.file_data_public = None
                fileupload.save()
              # Formatting google drive string
                str1 =  fileupload.file_data_private.url
                str2 = str1.replace("https://drive.google.com/file/d/","https://docs.google.com/uc?id=")
                str3 = str2.replace("/view?usp=drivesdk","")
                str3 = str1
              #  form = doc_f_docmaster(instance=form)
              #  form.file_name = fileupload.file_data
                docupload = doc_f_files()
                return render(request, 'docs/adddoc.html', {'form': form , 'file' : docupload , 'attlink':str3  })
        return redirect('Doc_List')
    else:
        form = doc_f_docmaster()
        docupload = doc_f_files()
        return render(request, 'docs/adddoc.html', {'form': form , 'file' : docupload }) 
    
def doclist(request):
    doc_list = doc_m_docmaster.objects.order_by('-doc_area')
    table = doc_t_docmaster(doc_list)
    RequestConfig(request).configure(table)

    doc_list1 = doc_m_files.objects.order_by('-id')
    table1 = doc_t_files(doc_list1)
    RequestConfig(request).configure(table1)

    return render(request, 'docs/doclist.html', {'table': table,'table1':table1})

def displaydoc(request,doc_id):
    post = get_object_or_404(doc_m_docmaster, pk=doc_id) 
    try:
       form = doc_f_docmaster(instance=post)
       if request.user.is_authenticated():
           post.doc_public = post.doc_public.replace("[private]","")
           post.doc_public = post.doc_public.replace("[/private]","")
       else:
           post.doc_public = mask_private(post.doc_public)
       return render(request, 'docs/displaydoc.html', {'form': post})
    except Stock.DoesNotExist:
       raise Http404("Document not exist")

def changedoc(request,doc_id):
    post = get_object_or_404(doc_m_docmaster, pk=doc_id)
    if request.method == "POST":
        form = doc_f_docmaster(request.POST, instance=post) 
        if form.is_valid():
            try:
                fileupload = doc_m_files(file_data_public=request.FILES['file_data_private'])
                fileupload = populatefile_db(fileupload)
            except:
                fileupload = None
            if 'delete_stock' in request.POST:
                # Stock Deleted
                post.delete()    
            elif 'change_stock' in request.POST: 
                # Stock Changes         
                form.save()
            elif 'upload_public' in request.POST: 
                fileupload.file_name = fileupload.file_data_public.name
                fileupload.save()
              # Formatting google drive string
                str1 =  fileupload.file_data_public.url
                str2 = str1.replace("https://drive.google.com/file/d/","https://docs.google.com/uc?id=")
                str3 = str2.replace("/view?usp=drivesdk","")
              #  form = doc_f_docmaster(instance=form)
              #  form.file_name = fileupload.file_data
                docupload = doc_f_files()
                return render(request, 'docs/changedoc1.html', {'form': form , 'file' : docupload , 'attlink':str3  })
            elif 'upload_private' in request.POST: 
                fileupload.file_name = fileupload.file_data_public.name
                fileupload.file_data_private = fileupload.file_data_public
                fileupload.file_data_public = None
                fileupload.save()
              # Formatting google drive string
                str1 =  fileupload.file_data_private.url
                str2 = str1.replace("https://drive.google.com/file/d/","https://docs.google.com/uc?id=")
                str3 = str2.replace("/view?usp=drivesdk","")
                str3 = str1
              #  form = doc_f_docmaster(instance=form)
              #  form.file_name = fileupload.file_data
                docupload = doc_f_files()
                return render(request, 'docs/changedoc1.html', {'form': form , 'file' : docupload , 'attlink':str3  })
            return redirect('Doc_List')
    else:   
        try:
            form = doc_f_docmaster(instance=post)
            docupload = doc_f_files()
            return render(request, 'docs/changedoc1.html', {'form': form , 'file' : docupload})
        except Stock.DoesNotExist:
            raise Http404("Document doesnt exist")


def mask_private(content):
    s = content
    first = "[private]"
    last = "[/private]"
    nos = s.count(first)
    count = 0
    try:
        while count < nos :
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            str1 = first + s[start:end] + last
            s = s.replace(str1," <div class='alert alert-danger'><strong> Login Required </strong></div>") 
            count = count + 1
        return s
    except ValueError:
        return ""

def populatefile_db(fileupload):
    fileupload.file_name = fileupload.file_data_public.name
    fileupload.file_url = fileupload.file_data_public.url
    str1 =  fileupload.file_data_public.url
    str2 = str1.replace("https://drive.google.com/file/d/","")
    str3 = str2.replace("/view?usp=drivesdk","")
    fileupload.file_gname = str3
    return(fileupload)