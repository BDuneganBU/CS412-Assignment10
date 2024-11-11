from django.shortcuts import render

# Create your views here.
# marathon_analytics/views.py
#
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from . models import Result
class ResultsListView(ListView):
    '''View to display marathon results'''
    template_name = 'marathon_analytics/results.html'
    model = Result
    context_object_name = 'results'
    def get_queryset(self):
        
        # limit results to first 25 records (for now)
        qs = super().get_queryset()
        return qs[:25]