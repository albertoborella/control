from django.contrib import admin
from django.urls import path
from auditorias.views import AuditoriaList

urlpatterns = [
    path('', AuditoriaList.as_view(), name = 'auditoria_list'),
]