from django.db import models
# Create your models here.
class Negocio(models.Model):
    nombre=models.CharField(max_length=50)#este es el str
    cuit=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.cuit)

class Empleado(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    cargo= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.apellido
        
class Producto(models.Model):
    categoria= models.CharField(max_length=50)
    precio= models.IntegerField()
    vencimiento= models.DateField()

    def __str__(self):
        return self.categoria+" "+str(self.precio)+" "+str(self.vencimiento)