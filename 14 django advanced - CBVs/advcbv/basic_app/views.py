from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
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

class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION from TemplateView!'
        return context
