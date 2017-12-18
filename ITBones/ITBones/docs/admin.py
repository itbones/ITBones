from django.contrib import admin
# Register your docs models here.
from .models import *

admin.site.register(doc_m_docmaster)
admin.site.register(doc_m_files)
