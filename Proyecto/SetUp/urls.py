from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home),
    path('ingresarProducto',views.ingresarProducto),
    path('accounts/',include('django.contrib.auth.urls')),
    path('salir/',views.salir, name="salir"),
    path('ingresarInventario',views.ingresarInventario),
    path('eliminarProducto/<codigo>',views.eliminarProducto),
    path('edicionProducto/<codigo>',views.edicionProducto),
    path('actualizarProducto/',views.actualizarProducto),
    path('ingresarProveedor',views.ingresarProveedor),
    path('registrarProveedor',views.registrarProveedor),
    path('eliminarProveedor/<codigo>',views.eliminarProveedor),
    path('editarProveedor/<codigo>',views.editarProveedor),
    path('actualizarProveedor/',views.actualizarProveedor)
]


   