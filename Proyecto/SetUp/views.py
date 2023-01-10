from django.shortcuts import render,redirect

from SetUp.models import Base, Provedor

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.




def salir(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    Inventario = Base.objects.all()
    
    return render(request,"gestionInventario.html",{"Inventario":Inventario})

@login_required
def ingresarInventario(request):
    return render(request, 'ingresarProducto.html')

@login_required
def ingresarProducto(request):
    codigo = request.POST['txtCodigo']
    producto = request.POST['txtProducto']
    categoria = request.POST['txtCategoria']
    inv_inicial = request.POST['numInicial']
    inv_recibido = request.POST['numRecibido']
    productos_vendido = 0

    inventario = Base.objects.create(codigo=codigo, producto=producto,categoria=categoria,inventario_inicial=inv_inicial,inventario_recibido=inv_recibido,productos_vendido=productos_vendido)
    return redirect('/')

@login_required
def edicionProducto(request,codigo):
    producto = Base.objects.get(codigo=codigo)
    return render(request,"edicionProducto.html",{"producto":producto})

@login_required
def eliminarProducto(request,codigo):
    producto = Base.objects.get(codigo=codigo)
    producto.delete()
    return redirect('/')

@login_required
def actualizarProducto(request):
    codigo = request.POST['txtCodigo']
    producto = request.POST['txtProducto']
    categoria = request.POST['txtCategoria']
    inv_inicial = request.POST['numInicial']
    inv_recibido = request.POST['numRecibido']
    inv_vendido = request.POST['numVendido']

    actualizar = Base.objects.get(codigo=codigo)
    actualizar.producto = producto
    actualizar.categoria = categoria
    actualizar.inventario_inicial = inv_inicial
    actualizar.inventario_recibido = inv_recibido
    actualizar.productos_vendido = inv_vendido
    actualizar.save()
    
    return redirect('/')

@login_required
def ingresarProveedor(request):
    proveedor = Provedor.objects.all()
    return render(request,'ingresarProveedor.html',{'proveedor':proveedor})

@login_required
def registrarProveedor(request):
    codigo = request.POST['txtCodigo']
    proveedor = request.POST['txtProveedor']
    direccion = request.POST['txtDireccion']
    estado = request.POST['txtEstado']
    codigo_producto = request.POST['txtCodigoProducto']

    Provedor.objects.create(codigo = codigo, proveedor=proveedor,direccion=direccion,Estado=estado,codigo_producto=codigo_producto)
    return redirect('/')

@login_required
def eliminarProveedor(request,codigo):
    proveedor = Provedor.objects.get(codigo=codigo)
    proveedor.delete()

    return redirect('/')

@login_required
def editarProveedor(request,codigo):
    proveedor = Provedor.objects.get(codigo=codigo)
    return render(request,"edicionProveedor.html",{"proveedor":proveedor})

@login_required
def actualizarProveedor(request):
    codigo = request.POST['txtCodigo']
    proveedor = request.POST['txtProveedor']
    direccion = request.POST['txtDireccion']
    estado = request.POST['txtEstado']
    codigo_producto = request.POST['txtCodigoProducto']

    actualizar = Provedor.objects.get(codigo=codigo)
    actualizar.proveedor = proveedor
    actualizar.direccion = direccion
    actualizar.Estado = estado
    actualizar.codigo_producto = codigo_producto
    actualizar.save()

    return redirect('/')