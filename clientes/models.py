from django.db import models

class Cliente(models.Model):
    RUBRO_CHOICE = (
    (1,'Lacteos'),
)
    
    razon_social = models.CharField('Razón Social', max_length=50, unique=True)
    codigo = models.CharField('Código', max_length=10, blank=True, null=True)
    rubro = models.IntegerField('Rubro', choices=RUBRO_CHOICE, default=1)
    ubicacion = models.CharField('Ubicación', max_length=100, blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=15, blank=True, null=True)
    persona_contacto = models.CharField('Persona de contacto', max_length=100, blank=True, null=True)
    celular_contacto = models.CharField('Celular de contacto', max_length=15, blank=True, null=True)
    created_at = models.DateTimeField('Fecha de inicio de contrato',auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de modificación', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['razon_social']

    def __str__(self):
        return self.razon_social

