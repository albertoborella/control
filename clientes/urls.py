from django.urls import path
from .views import ClienteList, ClienteCreate, Dashboard_Cliente1

urlpatterns = [
    path('clientes/', ClienteList.as_view(), name='cliente_list'),
    path('cliente/nuevo/', ClienteCreate.as_view(), name='cliente_create'),
    path('cliente1/', Dashboard_Cliente1.as_view(), name='cliente1'),
]