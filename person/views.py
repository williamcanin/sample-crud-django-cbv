# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import PersonModel

# Create your views here.


class PersonList(ListView):
    model = PersonModel
    template_name = 'person/person_list.html'


class PersonDetail(DetailView):
    model = PersonModel
    template_name = 'person/person_detail.html'


class PersonUpdate(UpdateView):
    model = PersonModel
    fields = '__all__'
    template_name = 'person/person_form.html'
    success_url = reverse_lazy('person_list')


class PersonDelete(DeleteView):
    model = PersonModel
    fields = '__all__'
    template_name = 'person/person_delete_confirm.html'
    success_url = reverse_lazy('person_list')


class PersonCreate(CreateView):
    model = PersonModel
    fields = '__all__'
    template_name = 'person/person_form.html'
    success_url = reverse_lazy('person_list')
