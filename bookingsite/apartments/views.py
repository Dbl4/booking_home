from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Apartment


class IndexListView(ListView):
    model = Apartment
    template_name = 'apartments/index.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Квартирное бюро'
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(IndexListView, self).dispatch(request, *args, **kwargs)
