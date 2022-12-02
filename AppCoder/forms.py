from django import forms


class NegocioForm(forms.Form):
    nombre=forms.CharField(max_length=50)#este es el str
    cuit=forms.IntegerField()

class EmpleadoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    cargo= forms.CharField(max_length=50)

class ProductoForm(forms.Form):
    categoria= forms.CharField(max_length=50)
    precio= forms.IntegerField()
    vencimiento= forms.DateField()
   