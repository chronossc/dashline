from django import forms
from models import TimeLine, Entry

class TimeLineForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        exclude = ('slug', 'date_created', 'owner')        