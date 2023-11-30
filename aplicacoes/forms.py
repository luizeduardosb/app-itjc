from django import forms

from .models import Email

class salvar(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('nome', 'email')