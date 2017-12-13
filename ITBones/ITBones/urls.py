"""
Definition of urls for ITBones.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from django.conf.urls import include, url
from django.contrib import admin

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from ITBones import money
from ITBones import webmark

urlpatterns = [
    # Examples:
     url(r'^$', app.views.home, name='home'),
   # url(r'^$', app.views.nse, name='nse'),
   url(r'^signup/$', app.views.signup, name='signup'),
    url(r'^money/', include('ITBones.money.urls')),
    url(r'^webmark/', include('ITBones.webmark.urls')),
    url(r'^nse/', include('ITBones.nse.urls')),
    url(r'^docs/', include('ITBones.docs.urls')),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Social Media login
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
