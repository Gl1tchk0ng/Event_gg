from django.forms import ModelForm
from .models import Eventdata

class addevent(ModelForm):
    class Meta:
        model = Eventdata
        fields = '__all__'
