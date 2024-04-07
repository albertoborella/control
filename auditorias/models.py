from django.db import models
from clientes.models import Cliente


class Auditoria(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField('Fecha de inicio', blank=False, null=False)
    auditor_lider = models.CharField('Auditor Líder', max_length=50, blank=False, null=False)
    otros_auditores = models.CharField('Otros Auditores', max_length=50, blank=True, null=True)
    representante_cliente = models.CharField('Representantes del Cliente Auditado', max_length= 150,blank=False, null=False)
    alcance = models.CharField('Alcance', max_length=500, blank=False, null=False)
    criterio = models.CharField('Criterio', max_length=500, blank=False, null=False)
    objetivo = models.CharField('Objetivo', max_length=500, blank=False, null=False)
    estado = models.BooleanField('Auditoría Finalizada', default=False)
    created_add = models.DateTimeField('Fecha de inicio de auditoría',auto_now_add=True)

    class Meta:
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return self.auditor_lider
    
class Evidencia(models.Model):
    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE)
    evidencia = models.CharField('Edidencia Objetiva', max_length=500, blank=False, null=False)
    ampliar_evidencia = models.TextField('Ampliar evidencia')

    class Meta:
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'
        ordering = ['-evidencia']

    def __str__(self):
        return self.evidencia
    
class No_conforme(models.Model):
    nc = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    texto = models.TextField('No Conformidad', blank=False, null=False)
    criterio_evidencia = models.CharField('Criterio', max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'No Conformidad'
        verbose_name_plural = 'No Conformidades'
        ordering = ['-texto']

    def __str__(self):
        return self.criterio
