from django.db import models
from django.forms import ModelForm
from .models import record, AllTeam, MyTeam


class recordForm(ModelForm):
    class Meta:
        model = record
        fields = '__all__'
        exclude = ['team',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder':'ผู้ทำรายการ'})
       
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control','placeholder':'รายละเอียด'})
        self.fields['type'].widget.attrs.update({'class': 'form-control','placeholder':'ผู้ทำรายการ'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control','placeholder':'จำนวน'})

class CreateTeamForm(ModelForm):
    class Meta:
        model = AllTeam
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder':'ชื่อทีม'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control','placeholder':'URL'})
