from django import forms
from .models import QalaData

class QalaDataFrom(forms.ModelForm):
    class Meta:
        model = QalaData
        fields = '__all__'