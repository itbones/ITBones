# tutorial/tables.py
import django_tables2 as tables
from .models import m_webmark
from django_tables2.utils import A  # alias for Accessor

class t_webmark(tables.Table):
    topic = tables.LinkColumn('webmark_display', args=[A('pk')])
    class Meta:
        model = m_webmark
        fields = ('folder','topic','addinfo',)     # closing , is very important
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
