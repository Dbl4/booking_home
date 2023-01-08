from django.views.generic import ListView, DetailView

from .models import Apartment, Messenger, Contact


class IndexListView(ListView):
    model = Apartment
    template_name = 'apartments/index.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Квартирное бюро'
        return context


class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartments.html'
    context_object_name = 'apartment'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(ApartmentDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Квартирное бюро | Квартиры'
        return context


# class ContactListView(ListView):
#     model = Contact
#     template_name = 'apartments/base.html'
#
#     def get_context_data(self, object_list=None, **kwargs):
#         context = super(ContactListView, self).get_context_data(**kwargs)
#         context['messengers'] = Messenger.objects.all()
#         return context