from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class AuditoriaList(ListView):
    model = Auditoria
    template_name = 'auditorias/auditoria_list.html'
    context_object_name = 'auditorias'
    queryset = Auditoria.objects.all()


