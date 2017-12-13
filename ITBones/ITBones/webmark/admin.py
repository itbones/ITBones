from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(m_webmaster)
admin.site.register(m_webitem)
admin.site.register(m_webmark)