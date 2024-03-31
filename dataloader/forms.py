from django.forms import ModelForm
from .models import Eventdata
from django import forms

class addevent(ModelForm):
    class Meta:
        model = Eventdata
        fields = '__all__'

class EventSearchForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    user_latitude = forms.FloatField(required=False)
    user_longitude = forms.FloatField(required=False)