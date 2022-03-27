from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.db import models,connection



def register(request):
    return render(request, 'account/register.html')

def admin(request):

    return render(request, 'map/index.html')
def client(request):

    return render(request, 'map/index2.html')

class client_register(CreateView):
    model = User
    form_class = ClientUserSignUpForm
    template_name = 'account/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/accounts/login')

class admin_register(CreateView):
    model = User
    form_class = AdminUserSignUpForm
    template_name = 'account/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/accounts/login')


def login_request(request):
    # attrs = {
    # 'name': models.CharField(max_length=32),
    # '__module__': 'accounts.models'
    # }
    # Animal = type("Animal", (models.Model,), attrs)
    # with connection.schema_editor() as schema_editor:
    #     schema_editor.create_model(Animal)
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_admin:
                    login(request,user)
                    return redirect('/accounts/admin-page')
                if not user.is_admin:
                    login(request,user)
                    return redirect('/accounts/client-page')
                return redirect('accounts/login')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'account/login.html',context={'form':AuthenticationForm()})
    
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

