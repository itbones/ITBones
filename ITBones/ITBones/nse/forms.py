# nse forms
from django import forms

from .models import nse_m_stocklist,nse_m_stocknews
from .forms import *
from bootstrap3_datetime.widgets import DateTimePicker

class nse_f_stocklist(forms.ModelForm):

    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','buyprice','buyqty','buydate','notes','notval1','notval2','notval3',)
      #  fields = '__all__'
       # exclude = ('currprice','finalval','currvalue','stock_desc',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        widgets = {
           'stock_code' : forms.TextInput(attrs={'readonly':'readonly'}),
           'buydate': forms.DateInput(attrs={'type': 'date'}),
            'notes' : forms.Textarea(attrs={'style': 'height: 7em;'})
        }

class nse_f_sellstock(forms.ModelForm):

    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','buyprice','buydate','notes','buyqty','sellqty','sellprice','selldate',)
      #  fields = '__all__'
       # exclude = ('currprice','finalval','currvalue','stock_desc',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'buyprice': ('Purchase Price'),
            'buydate': ('Purchase Date'),
            'notval1': ('Notification Value'),
            'notes': ('Notes'),
        }
        widgets = {
           'stock_code' : forms.TextInput(attrs={'readonly':'readonly'}),
           'buyprice' : forms.TextInput(attrs={'readonly':'readonly'}),
           'buyqty' : forms.TextInput(attrs={'readonly':'readonly'}),
           'buydate' : forms.TextInput(attrs={'readonly':'readonly'}),
           'selldate': forms.DateInput(attrs={'type': 'date'}),
           'sellqty': forms.TextInput(attrs={'required': 'required'}),
            'notes' : forms.Textarea(attrs={'style': 'height: 7em;'})
        }

class nse_f_addwatchlititem(forms.ModelForm):

    class Meta:
        model = nse_m_stocklist
        fields = ('stock_code','notval1','notval2','notval3','notes',)
      #  fields = '__all__'
       # exclude = ('currprice','finalval','currvalue','stock_desc',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'notval1': ('Sell Notif Price'),
            'notval2': ('Buy Notif Price'),
            'notval3': ('Stop Loss Notif'),
            'notes': ('Notes'),
        }
        widgets = {
            'notes' : forms.Textarea(attrs={'style': 'height: 7em;'})
        }

class nse_f_stocknews(forms.ModelForm):

    class Meta:
        model = nse_m_stocknews
        fields = '__all__'
       # exclude = ('currprice','finalval','currvalue','stock_desc',)
        labels = {
            'stock_code': ('NSE Stock Code'),
            'notedate': ('Notes Date'),
            'notes': ('Notes'),
        }
        widgets = {
            'stock_code' : forms.TextInput(attrs={'readonly':'readonly'}),
            'notedate': forms.DateInput(attrs={'type': 'date'}),
            'notes' : forms.Textarea(attrs={'style': 'height: 7em;'})
        }