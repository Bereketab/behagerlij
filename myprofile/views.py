from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FamilyMemberFormSet
from .models import Table


class ProfileList(ListView):
    model = Table


class ProfileCreate(CreateView):
    model = Table
    fields = ['table_name']

class ProfileFamilyMemberCreate(CreateView):
    model = Table
    fields = ['table_name']
    success_url = reverse_lazy('myprofile:table-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['feilds'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['feilds'] = FamilyMemberFormSet()
        return data
        
    # Animal = type("Animal", (models.Model,), attrs)
    # with connection.schema_editor() as schema_editor:
    #     schema_editor.create_model(Animal)
    def form_valid(self, form):
        context = self.get_context_data()
        feilds = context['feilds']
        with transaction.atomic():
            # self.object = form.save()

            if feilds.is_valid():
                feilds.instance = self.object
                # feilds.save()
                attrs = {}
# for j in xrange(10):
#     key_j = 'key_{}'.format(j)  # a string depending on j
#     res[key_j] = j**2
                for i in feilds.cleaned_data:
                    field_name = '{}'.format(i['field_name'])
                    field_data_type = '{}'.format(i['field_data_type'])
                    field_max_length = '{}'.format(i['field_max_length'])
                    attrs[field_name] = 'models.'+field_data_type+'(max_length='+field_max_length+'),'
                    # print(key)

           
                # attrs['__module__']='accounts.models'
                print(attrs)
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Table
    success_url = '/'
    fields = ['table_name']


class ProfileFamilyMemberUpdate(UpdateView):
    model = Table
    fields = ['table_name']
    success_url = reverse_lazy('myprofile:table-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['feilds'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['feilds'] = FamilyMemberFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        feilds = context['feilds']
        with transaction.atomic():
            self.object = form.save()

            if feilds.is_valid():
                feilds.instance = self.object
                feilds.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Table
    success_url = reverse_lazy('myprofile:table-list')
