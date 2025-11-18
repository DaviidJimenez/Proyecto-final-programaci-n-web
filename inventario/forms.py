from django import forms
from .models import Producto, Marca

# FORMULARIO PRODUCTO
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


# FORMULARIO MARCA
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
