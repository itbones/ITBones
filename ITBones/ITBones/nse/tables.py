# nse tables.py
import django_tables2 as tables
from .models import nse_m_stocklist,nse_m_summarysheet,nse_m_stocknews
from django_tables2.utils import A  # alias for Accessor


class nse_t_stocklist(tables.Table):
    def __init__(self, *args, **kwargs):
        super(nse_t_stocklist, self).__init__(*args, **kwargs)
       
    def render_realpos(self, value, column):
        zvalue = int(value)
        if zvalue < 0:
            column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
        else:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        return value

    stock_code = tables.LinkColumn('maintain', args=[A('pk')])
   # sell_key = tables.LinkColumn(viewname='sell', args=[A('pk')],text='Sell',attrs={'a': {'style': 'color: red;'}})
    sell_key = tables.TemplateColumn('<a href="sell/{{record.id}}">Sell</a>')
   # realpos = tables.Column( footer=lambda table: sum(x['realval'] for x in table.data))


    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','buyprice','buyqty','buyvalue','buydate','currprice','currvalue','realpos','notes','sell_key',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        attrs = {'class': 'paleblue'}

class nse_t_pllist(tables.Table):
    def __init__(self, *args, **kwargs):
        super(nse_t_pllist, self).__init__(*args, **kwargs)
       
    def render_plfinal(self, value, column):
        zvalue = int(float(value))
        if zvalue < 0:
            column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
        else:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        return value
    period = tables.Column (accessor='holdingperiod',verbose_name='Held Days')
    periodret = tables.Column (accessor='periodret',verbose_name='% Ret')
    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','buyprice','buyqty','buyvalue','buydate','sellprice','selldate','sellqty','sellvalue','plfinal','notes',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        attrs = {'class': 'paleblue'}

class nse_t_watchlist(tables.Table):
    notval1 = tables.Column (verbose_name='Buy more  Notif')
    notval2 = tables.Column (verbose_name='Sell Notif')
    notval3 = tables.Column (verbose_name='Stop Loss Notif')
    Delete = tables.TemplateColumn('<a href="watchlist/delete/{{record.id}}">Delete</a>')
    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','currprice','notval1','notval2','notval3','notes',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        attrs = {'class': 'paleblue'}

class nse_t_summarysheet(tables.Table):
    def __init__(self, *args, **kwargs):
        super(nse_t_summarysheet, self).__init__(*args, **kwargs)
       
    def render_realpos(self, value, column):
        zvalue = int(float(value))
        if zvalue < 0:
            column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
        else:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        return value
    stock_code = tables.TemplateColumn('<a href="stocklist/{{record.stock_code}}">{{record.stock_code}}</a>')
    #stock_code = tables.Column ('maintain', args=[A('stock_code')],verbose_name='Instrument')
    totbuyqty = tables.Column (verbose_name='Qty')
    avgbuyprice = tables.Column (verbose_name='Buy Price')
    currprice = tables.Column (verbose_name='Curr Price')
    currvalue = tables.Column (verbose_name='Curr Val')
    realpos = tables.Column (verbose_name='P/L')
    stock_news = tables.TemplateColumn('<a href="stocklist/addstocknews/{{record.stock_code}}">Add</a>')
    class Meta:
        model = nse_m_summarysheet
        fields = ('stock_code','totbuyqty','avgbuyprice','currprice','currvalue','realpos','stock_news',)
        attrs = {'class': 'paleblue'}

class nse_t_stocknews(tables.Table):

    class Meta:
        model = nse_m_stocknews
        fields = ('notedate','notes',)
        attrs = {'class': 'paleblue'}

class nse_t_summary(tables.Table):
    def __init__(self, *args, **kwargs):
        super(nse_t_summary, self).__init__(*args, **kwargs)
       
    def render_retval(self, value, column):
        zvalue = int(value)
        if zvalue < 0:
            column.attrs = {'td': {'bgcolor': 'LightSalmon' , 'style' : 'font-size: 12px;'}}
        else:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        return value

    invval = tables.Column (verbose_name='Invested Value')
    curval = tables.Column (verbose_name='Current Value')
    retval = tables.Column (verbose_name='Return Value')
    retper = tables.Column (verbose_name='Return %')
    class Meta:
        attrs = {'class': 'paleblue'}
