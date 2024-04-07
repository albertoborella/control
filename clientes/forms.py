from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razon_social','codigo','rubro','ubicacion','telefono','persona_contacto','celular_contacto']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['razon_social'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['codigo'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['rubro'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['ubicacion'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['persona_contacto'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['celular_contacto'].widget.attrs.update({
            'class':'form-control',
        })
