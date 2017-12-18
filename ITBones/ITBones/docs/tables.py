# docs tables.py
import django_tables2 as tables
from .models import doc_m_docmaster,doc_m_files
from django_tables2.utils import A  # alias for Accessor


class doc_t_docmaster(tables.Table):
   # def __init__(self, *args, **kwargs):
   #     super(doc_t_docmaster, self).__init__(*args, **kwargs)
       
   # def render_realpos(self, value, column):
   #     zvalue = int(value)
   #     if zvalue < 0:
   #         column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
   #     else:
   #         column.attrs = {'td': {'bgcolor': 'lightgreen'}}
   #     return value

    doc_sub = tables.LinkColumn('Display_Doc', args=[A('pk')])
   ## sell_key = tables.LinkColumn(viewname='sell', args=[A('pk')],text='Sell',attrs={'a': {'style': 'color: red;'}})
    chg_key = tables.TemplateColumn('<a href="change/{{record.id}}">Modify</a>')
   ## realpos = tables.Column( footer=lambda table: sum(x['realval'] for x in table.data))


    class Meta:
        model = doc_m_docmaster
        fields = ('doc_area','doc_subarea','doc_tag','doc_sub',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        attrs = {'class': 'paleblue'}

#class nse_t_pllist(tables.Table):
#    def __init__(self, *args, **kwargs):
#        super(nse_t_pllist, self).__init__(*args, **kwargs)
       
#    def render_plfinal(self, value, column):
#        zvalue = int(float(value))
#        if zvalue < 0:
#            column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
#        else:
#            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
#        return value
#    period = tables.Column (accessor='holdingperiod',verbose_name='Held Days')
#    periodret = tables.Column (accessor='periodret',verbose_name='% Ret')
#    class Meta:
#        model = nse_m_stocklist
#        fields = ('stock_code','buyprice','buyqty','buyvalue','buydate','sellprice','selldate','sellqty','sellvalue','plfinal','notes',)
#        labels = {
#            'stock_code': ('NSE Stock Code'),
#            'buyprice': ('Purchase Price'),
#            'buydate': ('Purchase Date'),
#            'notval1': ('Notification Value'),
#            'notes': ('Notes'),
#        }
#        attrs = {'class': 'paleblue'}

#class nse_t_watchlist(tables.Table):
#    notval1 = tables.Column (verbose_name='Buy Notif')
#    notval2 = tables.Column (verbose_name='Sell Notif')
#    notval3 = tables.Column (verbose_name='Breakeven Notif')
#    class Meta:
#        model = nse_m_stocklist
#        fields = ('stock_code','currprice','notval1','notval2','notval3','notes',)
#        labels = {
#            'stock_code': ('NSE Stock Code'),
#            'buyprice': ('Purchase Price'),
#            'buydate': ('Purchase Date'),
#            'notval1': ('Notification Value'),
#            'notes': ('Notes'),
#        }
#        attrs = {'class': 'paleblue'}
class doc_t_files(tables.Table):
    class Meta:
        model = doc_m_files
        fields = ('id','file_name','file_data',)
        attrs = {'class': 'paleblue'}

