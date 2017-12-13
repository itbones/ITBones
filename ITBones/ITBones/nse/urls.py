from django.conf.urls import url

from . import views
app = 'nse'
urlpatterns = [
    url(r'^$', views.summarysheet, name='Stock_Summary'),
    url(r'^stocklist/(?P<stockcode>\w+)/additem$', views.additem, name='Add Stock Item'), #Navigation from stocklist
    url(r'^allstocklist/additem$', views.additem, name='Add Stock Item'), #Navigation from All stocklist
    url(r'^stocklist/(?P<stockcode>\w+)/$', views.mystock, name='My_Stock_Listing'),
    url(r'^allstocklist/$', views.mystock, name='My_Stock_Listing_All'),
    url(r'^summary$', views.summarysheet, name='My_Stock_Summary'),
    url(r'^additem$', views.additem, name='Add Stock Item'), #Navigation from summary sheet
    url(r'^addwatchlist$', views.addwatchlistitem, name='Add_Watch_list'),
    url(r'^plstatement$', views.plstatement, name='P_L_Statement'),
    url(r'^notif$', views.sendemail, name='send_email'),
    url(r'^watchlist$', views.watchlist, name='Watch_List'),
    url(r'^watchlist/delete/(?P<stock_id>[0-9]+)/$', views.deletewatchlist, name='Delete_Watch_List'),
    url(r'^(?P<stock_id>[0-9]+)/$', views.maintainitem, name='maintain'),
    url(r'^allstocklist/(?P<stock_id>[0-9]+)/$', views.maintainitem, name='maintain'),
    url(r'^sell/(?P<stock_id>[0-9]+)/$', views.sellitem, name='sell'),
    url(r'^allstocklist/sell/(?P<stock_id>[0-9]+)/$', views.sellitem, name='sell'),
    url(r'^stocklist/(?P<stockcode>\w+)/sell/(?P<stock_id>[0-9]+)/$', views.sellitem, name='sell'),
    # Stock News
    url(r'^stocklist/(?P<stockcode>\w+)/addstocknews/$', views.addstocknews, name='Add_Stock_News'),
    url(r'^stocklist/addstocknews/(?P<stockcode>\w+)/$', views.addstocknews, name='Add_Stock_News'),
 #   url('(\d+)/', views.sellitem, name='sell'),
 #   url('(\d+)/', views.maintainitem, name='maintain'),
]
