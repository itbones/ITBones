from django.conf.urls import url

from . import views
app = 'money'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addstock$', views.addstock, name='Add Stock'),
    url(r'^sendemail$', views.sendemail, name='Send Email'),
    url(r'^(?P<stockid>[0-9]+)/$', views.displaystock_v, name='Display Details'),
]
