from django.shortcuts import render
from django.views.generic import (
                                View, TemplateView,
                                 ListView, DetailView,
                                 CreateView, UpdateView,
                                 DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

# Create your views here.



class Indexview(TemplateView):

    template_name = 'index.html' 

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['inject'] = 'basic inject'
        return context

class SchoolListview(ListView):
    content_object_name = 'schools'
    model = models.School

    



class SchoolDetailview(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateview(CreateView):
    fields = ('name', 'principal','location' )
    model = models.School

class SchoolUpdateview(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteview(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')


