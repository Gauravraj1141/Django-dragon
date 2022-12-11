from django import forms
from .models import logform


class myform(forms.ModelForm):

    class Meta:
        model = logform
        fields = ('name', 'email', 'phone', )
