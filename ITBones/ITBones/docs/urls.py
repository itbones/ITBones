from django.conf.urls import url
# docs documentation
from . import views
app = 'docs'
urlpatterns = [
    url(r'^$', views.doclist, name='Doc_List'),
    url(r'^adddoc$', views.adddoc, name='Add_Docs'),
    #url(r'^addwatchlist$', views.addwatchlistitem, name='Add_Watch_list'),
    #url(r'^plstatement$', views.plstatement, name='P_L_Statement'),
    #url(r'^notif$', views.sendemail, name='send_email'),
    #url(r'^watchlist$', views.watchlist, name='Watch_List'),
    url(r'^(?P<doc_id>[0-9]+)/$', views.displaydoc, name='Display_Doc'),
    url(r'^change/(?P<doc_id>[0-9]+)/$', views.changedoc, name='Change_Doc'),
 #   url('(\d+)/', views.sellitem, name='sell'),
 #   url('(\d+)/', views.maintainitem, name='maintain'),
]
