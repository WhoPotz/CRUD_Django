from django.db import models

# Create your models here.
class Base(models.Model):
    codigo = models.CharField(primary_key= True,max_length = 6)
    producto = models.CharField(max_length =100)
    categoria = models.CharField(max_length =100)
    inventario_inicial = models.IntegerField()
    inventario_recibido = models.IntegerField()
    productos_vendido = models.IntegerField(blank=True,null=True)

    def __str__ (self):
        texto = "{0}({1})"
        return texto.format(self.codigo,self.producto)

class Provedor(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    proveedor = models.CharField(max_length =50)
    direccion = models.CharField(max_length =50)
    Estado = models.CharField(max_length =50)
    codigo_producto = models.CharField(max_length = 6)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.codigo,self.proveedor)
