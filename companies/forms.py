from django import forms
from .models import Company, ServiceOrder, Service
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

STATE_CHOICES = STATE_CHOICES + ((None, '----'),)


#change name to model form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'uf', 'email','services']

class ServiceOrderModelForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['title', 'company', 'service']

class SearchModelForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    uf = forms.ChoiceField(choices=STATE_CHOICES, required=False, initial={None: '----'})
    email = forms.EmailField(max_length=100, required=False)

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title']