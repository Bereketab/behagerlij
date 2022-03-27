from django.urls import path
from .import  views

urlpatterns=[
     path('admin-page/',views.admin, name='admin-page'),
     path('client-page/',views.client, name='client-page'),
     path('register/',views.register, name='register'),
     path('customer_register/',views.client_register.as_view(), name='customer_register'),
     path('employee_register/',views.admin_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]