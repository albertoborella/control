from django.contrib import admin
from .models import Auditoria, Evidencia, No_conforme


class AuditoriaAdmin(admin.ModelAdmin):
    model = Auditoria
    list_display = ('cliente','fecha_inicio','auditor_lider','estado')
    readonly_fields=('created_add',)



admin.site.register(Auditoria,AuditoriaAdmin)
admin.site.register(Evidencia)
admin.site.register(No_conforme)


