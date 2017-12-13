from django import forms

from .models import *
from .forms import *

class f_webmark(forms.ModelForm):

    class Meta:
        model = m_webmark
        fields = ('folder','topic','addinfo','link','linkinfo')







