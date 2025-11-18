from django.contrib import admin
from .models import (
    Categoria, Proveedor, UnidadMedida, Marca,
    Almacen, Producto, MovimientoInventario
)

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(UnidadMedida)
admin.site.register(Marca)
admin.site.register(Almacen)
admin.site.register(Producto)
admin.site.register(MovimientoInventario)
