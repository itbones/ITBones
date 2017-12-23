
from app.models import  admin_visitor
from django.http import HttpRequest 
import datetime

def log_visitor(request):
    
    visitor_data = admin_visitor()
    visitor_data.ip_add = get_client_ip(request)
    
    if request.user.username == None:
        visitor_data.userid = 'Not Logged in'
    else:
        visitor_data.userid = request.user.username
    visitor_data.viewname = request.path
    i = datetime.datetime.now()
    #i = i.strftime('%Y-%m-%d')
    i = i.isoformat()
    visitor_data.logstamp = i
    visitor_data.save()
    return
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip