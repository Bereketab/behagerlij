from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class ClientUserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email = forms.EmailField(max_length=20)
    organization_name = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        client = ClientUser.objects.create(user=user)
        client.phone_number=self.cleaned_data.get('phone_number')
        client.location=self.cleaned_data.get('location')
        client.email=self.cleaned_data.get('email')
        client.organization_name=self.cleaned_data.get('organization_name')
        client.position=self.cleaned_data.get('position')
        client.save()
        return user

class AdminUserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        # user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admin = AdminUser.objects.create(user=user)
        admin.phone_number=self.cleaned_data.get('phone_number')
        admin.email=self.cleaned_data.get('email')
        admin.save()
        return user
