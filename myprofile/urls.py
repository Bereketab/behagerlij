from django.urls import path

from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='table-list'),
    path('table/add/', views.ProfileFamilyMemberCreate.as_view(), name='table-add'),
    path('table/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='table-update'),
    path('table/delete/<int:pk>', views.ProfileDelete.as_view(), name='table-delete'),
]
