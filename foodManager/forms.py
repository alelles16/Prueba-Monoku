from django import forms
from .models import Inventario

class InventarioForm(forms.ModelForm):

    cantidad = forms.IntegerField()

    class Meta:
        model = Inventario
        fields = ('cantidad',)