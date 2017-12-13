from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(nse_m_stocklist)
admin.site.register(nse_m_summarysheet)
admin.site.register(nse_m_stocknews)