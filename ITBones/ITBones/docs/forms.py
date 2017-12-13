# docs forms
from django import forms
from tinymce.widgets import TinyMCE
from .models import doc_m_docmaster
from .forms import *
from bootstrap3_datetime.widgets import DateTimePicker

class doc_f_docmaster(forms.ModelForm):
    doc_public = forms.CharField(widget=TinyMCE(attrs={'cols': 180, 'rows': 80}))
    doc_register = forms.CharField(widget=TinyMCE(attrs={'cols': 180, 'rows': 80}),required = False)
    doc_private = forms.CharField(widget=TinyMCE(attrs={'cols': 180, 'rows': 80}),required = False)
    doc_ref = forms.CharField(widget=TinyMCE(attrs={'cols': 180, 'rows': 40}),required = False)
    doc_sub = forms.CharField(widget=forms.TextInput(attrs={'size': '120', 'maxlength':'100'}))
    class Meta:
        model = doc_m_docmaster
       # fields = ('stock_code','buyprice','buyqty','buydate','notes','notval1','notval2','notval3',)
        fields = '__all__'
       # exclude = ('currprice','finalval','currvalue','stock_desc',)
        #labels = {
        #    'stock_code': ('NSE Stock Code'),
        #    'buyprice': ('Purchase Price'),
        #    'buydate': ('Purchase Date'),
        #    'notval1': ('Notification Value'),
        #    'notes': ('Notes'),
        #}
        #widgets = {
        #   'stock_code' : forms.TextInput(attrs={'readonly':'readonly'}),
        #   'buydate': forms.DateInput(attrs={'type': 'date'}),
        #    'notes' : forms.Textarea(attrs={'style': 'height: 5em;'})
        #}

