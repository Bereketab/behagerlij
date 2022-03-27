from dataclasses import Field
from django import forms
from django.forms import ModelChoiceField, inlineformset_factory
from .models import Table,Feilds



class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        exclude = ()

data_types =(
    ("string", "string"),
    ("nubmer", "number"),
)
class FeildsForm(forms.ModelForm):
    # field_data_type=forms.ChoiceField(choices = data_types)
    # field_max_length = forms.IntegerField()
    class Meta:
        model = Feilds
        exclude = ()



FeildsInlineFormset = inlineformset_factory(Table, Feilds,
                                            form=FeildsForm, extra=1)
  

