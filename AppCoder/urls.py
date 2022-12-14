from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path("negocio/", negocio, name="negocio"),# el primero es el url de la pagina, el segundo el nombre de la view, el tercero el nombre que va a llamar el boton en padre con jinja
    path("negocios/", negocios, name="negocios"),
    path("productos/", productos, name="productos"),
    path("empleados/", empleados, name="empleados"),
    path("", inicio,name='inicio'),
    path("negocioFormulario/", negocioFormulario, name="negocioFormulario"),
    path("productoFormulario/", productoFormulario, name="productoFormulario"),
    path("busquedaNegocio/", busquedaNegocio, name="busquedaNegocio"),
    path("buscar/", buscar, name="buscar"),
    path("leerEpleados/", leerEmpleados, name="leerEmpleados"),
    path("resultadosBusqueda/", buscar, name="resultadosBusqueda"),
    
]
