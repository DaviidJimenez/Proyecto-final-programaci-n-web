from django.urls import path
from . import views

urlpatterns = [

    # CRUD PRODUCTOS
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/crear/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', views.producto_edit, name='producto_edit'),
    path('productos/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),

    # CRUD MARCAS
    path('marcas/', views.marca_list, name='marca_list'),
    path('marcas/crear/', views.marca_create, name='marca_create'),
    path('marcas/editar/<int:pk>/', views.marca_update, name='marca_update'),
    path('marcas/eliminar/<int:pk>/', views.marca_delete, name='marca_delete'),
]
