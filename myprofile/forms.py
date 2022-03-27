from django.forms import ModelForm, inlineformset_factory

from .models import Table,Feilds


class ProfileForm(ModelForm):
    class Meta:
        model = Table
        exclude = ()


class FamilyMemberForm(ModelForm):
    class Meta:
        model = Feilds
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Table, Feilds,
                                            form=FamilyMemberForm, extra=1)
