from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse
from django.db import transaction
from django.urls import reverse_lazy

# Create your views here.
# def create_work(request):
#     return render(request,'account/worktype.html',)

class ProfileList(ListView):
    model = Table

class create_work(CreateView):
    model = Table
    fields = ['table_name']
    success_url = reverse_lazy('tables:create_work')
    # form_class = FeildsInlineFormset()

    def get_context_data(self, **kwargs):
        data = super(create_work, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FeildsInlineFormset(self.request.POST)
            attrs = {
                self.request.POST['table_name']: models.CharField(max_length=32),
                '__module__': 'accounts.models'
                }
            
                    # Animal = type("Animal", (models.Model,), attrs)
                    # with connection.schema_editor() as schema_editor:
                    #     schema_editor.create_model(Animal)
            
        else:
            data['familymembers'] = FeildsInlineFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        # for f in context['familymembers']: 
        #     # cd = f.cleaned_data
        #     # first_name = cd.get('first_name')
        #     print(f)
        print()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(create_work, self).form_valid(form)

class ProfileFamilyMemberUpdate(UpdateView):
    model = Table
    fields = ['table_name']
    success_url = reverse_lazy('table-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FeildsInlineFormset(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FeildsInlineFormset(instance=self.object)
        return data