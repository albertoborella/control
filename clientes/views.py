from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from .models import Cliente
from .forms import ClienteForm


class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_create.html'
    success_url = reverse_lazy('cliente_list')


class Dashboard_Cliente1(TemplateView):
    template_name = 'clientes/pag_cliente1.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = 'Ana Rocio'
        return context

