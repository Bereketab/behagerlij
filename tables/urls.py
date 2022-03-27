from django.urls import path
from .import  views
app_name = 'tables'
urlpatterns=[
     path('create-work/',views.create_work.as_view(), name='create_work'),
     path('table/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='table-update'),
     path('', views.ProfileList.as_view(), name='table-list'),
   
]