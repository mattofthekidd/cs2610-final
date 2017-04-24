from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic

from .models import Item
# Create your views here.
class ItemView(generic.ListView):
    template_name = 'final/item.html'
    context_object_name = 'table_item'
    def get_queryset(self):
        return Item.objects.order_by('-pub_date')[:5]
        
# class MainView(generic.DetailView):
#     model = Main
#     template_name = 'final/main.html'