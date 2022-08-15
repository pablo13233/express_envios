# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from principal.models import *

class ClienteAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    #list_display=['parte', 'activo']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['nombre_completo', 'celular',]
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['activo']
admin.site.register(Cliente, ClienteAdmin)

class EnvioAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    #list_display=['parte', 'activo']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['codigo']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['activo']
admin.site.register(Envio, EnvioAdmin)
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Rol)
admin.site.register(Empleado)
admin.site.register(EmpresaDiaContable)
admin.site.register(EmpresaEmpleado)
admin.site.register(ClienteRecibe)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Revendedor)
admin.site.register(EstadoEnvio)
admin.site.register(HistorialEnvio)
admin.site.register(EmpresaControlCaja)
admin.site.register(EmpresaDetalleCaja)
admin.site.register(EmpresaActividades)
admin.site.register(SeguimientoEnvio)
admin.site.register(EmpresaTipoGasto)
admin.site.register(EmpresaGasto)
admin.site.register(PagosCredito)
admin.site.register(ReciboCaja)
admin.site.register(ReciboContenedor)
admin.site.register(ReciboVehiculos)
admin.site.register(TipoMensajes)
admin.site.register(EmpresaMensaje)
admin.site.register(TipoContenido)
admin.site.register(TipoEnvio)

admin.site.register(TipoCaja)
admin.site.register(CajaPais)
admin.site.register(DetalleEnvio)
admin.site.register(Contenedor)
admin.site.register(UbicacionEmpleado)
admin.site.register(Camion)
