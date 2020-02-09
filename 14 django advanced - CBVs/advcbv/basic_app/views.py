from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, 
                                ListView, DetailView, 
                                CreateView, UpdateView, 
                                DeleteView)
from django.http import HttpResponse
from . import models

# Create your views here.
class SchoolListView(ListView):
    context_object_name = 'schools' # school_list (default by ListView if you are not setting)
    model = models.School
    

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' # school (default by DetailView)
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ['name', 'principal', 'location']

    # Exception Type:	TemplateDoesNotExist
    # Exception Value: basic_app/school_form.html

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ['name', 'principal']

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION from TemplateView!'
        return context
