from django import forms

from .models import Stock
from .forms import *

class PostStock(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_code','stock_name',)


