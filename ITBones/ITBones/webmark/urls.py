from django.conf.urls import url

from . import views
app = 'money'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addwebmark$', views.addwebmark, name='Add Web Mark'),
    url('(\d+)/', views.addwebmark, name='webmark_display'),
]
