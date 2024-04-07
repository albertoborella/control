from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('razon_social','codigo','persona_contacto','celular_contacto','created_at')
    readonly_fields=('created_at',)


admin.site.register(Cliente,ClienteAdmin)