from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca
from .forms import ProductoForm, MarcaForm


# CRUD PRODUCTOS
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'inventario/producto_form.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'inventario/producto_confirm_delete.html', {'producto': producto})



# CRUD MARCAS 
def marca_list(request):
    marcas = Marca.objects.all()
    return render(request, 'inventario/marca_list.html', {'marcas': marcas})

def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm()
    return render(request, 'inventario/marca_form.html', {'form': form})

def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'inventario/marca_form.html', {'form': form})

def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, 'inventario/marca_confirm_delete.html', {'marca': marca})
