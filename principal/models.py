# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import *
import sys
#reload(sys)
#sys.setdefaultencoding('utf8') //En python 3.X ya no es necesario

class AuthUser(models.Model):
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True,null=True)
	is_superuser = models.BooleanField()
	username = models.CharField(max_length=150)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	is_staff = models.BooleanField()
	is_active = models.BooleanField()
	date_joined = models.DateTimeField

	class Meta:
		managed = False
		db_table = 'auth_user'

class Rol(models.Model):
	rol = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.rol)

class UbicacionEmpleado(models.Model):
	ubicacion = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.ubicacion)

class Empleado(models.Model):
	nombres_empleado = models.CharField(max_length=50)
	apellidos_empleado = models.CharField(max_length=50)
	telefono_empleado = models.CharField(max_length=50)
	correo_empleado = models.EmailField()
	usuario =  models.ForeignKey(User,related_name='empleado_usuario',on_delete=models.CASCADE)
	rol_empleado =  models.ForeignKey(Rol,on_delete=models.CASCADE)
	usuario_registro = models.ForeignKey(User,related_name='empleado_usuario_registro',on_delete=models.CASCADE)
	#ubicacion = models.ForeignKey(UbicacionEmpleado, null=True, blank=True)
	def __str__(self):
		return '{} {}'.format(self.nombres_empleado,self.apellidos_empleado)

class Empresa(models.Model):
	codigo_empresa = models.CharField(max_length=5)
	nombre_empresa = models.CharField(max_length=100)
	slogan_empresa = models.CharField(max_length=100)
	logo_empresa = models.FileField(upload_to="logo_empresa/", null=True, blank=True)
	direccion_empresa = models.CharField(max_length=200)
	telefono_empresa = models.CharField(max_length =100)
	celular_empresa = models.CharField(max_length =100)
	correo_empressa = models.EmailField()
	usuario_registro = models.ForeignKey(User,related_name='empresa_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {}'.format(self.codigo_empresa,self.nombre_empresa)

class Revendedor(models.Model):
	nombre_completo = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=100, blank=True, null=True)
	nombre_empresa =  models.CharField(max_length=100, blank=True, null=True)
	direccion = models.CharField(max_length=100, blank=True, null=True)
	telefono_empresa = models.CharField(max_length=100, blank=True, null=True)
	celular_empresa = models.CharField(max_length=100, blank=True, null=True)
	correo = models.EmailField()
	logo = models.FileField(upload_to="logo_revendedor/", null=True, blank=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	es_revendedor = models.BooleanField(default=True)
	usuario_registro = models.ForeignKey(User,related_name='usuario_registro_revendedor', default= 1,on_delete=models.CASCADE)
	def __str__(self):
		return '{0}'.format(self.nombre_empresa)

class EmpresaDiaContable(models.Model):
	codigo_empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	fecha_apertura = models.DateTimeField(auto_now_add=True)
	valor_apertura = models.FloatField()
	valor_cierre = models.FloatField()
	valor_efectivo = models.FloatField()
	faltante = models.FloatField(default=0.00)
	usuario_registro = models.ForeignKey(User,related_name='empresa_dia_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {}'.format(self.fecha_apertura,self.valor_apertura)

class EmpresaEmpleado(models.Model):
	empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
	empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
	usuario_registro = models.ForeignKey(User,related_name='empresa_empleado_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {} | {}'.format(self.empresa,self.empleado,self.usuario_registro)

class Estados(models.Model):
	estado = models.CharField(max_length=100, blank=False, null=False)
	def __str__(self):
		return '{}'.format(self.estado)

class Cliente(models.Model):
	nombre_completo = models.CharField(max_length=100, blank=False, null=False)
	celular = models.CharField(max_length=15, blank=True, null=True)
	direccion = models.CharField(max_length=300, blank=True, null=True)
	usuario_registro = models.ForeignKey(User,related_name='usuario_registro',on_delete=models.CASCADE)
	#correo = models.EmailField(blank=True,null=True)
	empresa = models.ForeignKey(Empresa,blank=True,null=True,on_delete=models.CASCADE)
	revendedor = models.BooleanField(default=False) # si es true se mostrara en clientes revendedor
	revenedor_creo = models.ForeignKey(Revendedor, null=True,on_delete=models.CASCADE)
	estado = models.ForeignKey(Estados,blank=True,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{0} | {1}'.format(self.nombre_completo,self.celular)

class Pais(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	precio_pulgada_caja = models.FloatField(default=0.00)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

class Departamento(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	codigo = models.CharField(max_length=50, blank=False, null=False)
	pais = models.ForeignKey(Pais,on_delete=models.CASCADE)

	def __str__(self):
		return '{0} | {1} '.format(self.nombre,self.pais.nombre)

class ClienteRecibe(models.Model):
	cliente_envia = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	nombre_completo = models.CharField(max_length=100, blank=False, null=False)
	celular = models.CharField(max_length=50, blank=True, null=True)
	direccion = models.CharField(max_length=300, blank=True, null=True)
	pais = models.CharField(max_length=300, blank=True, null=True)
	departamento = models.CharField(max_length=300, blank=True, null=True)
	usuario_registro = models.ForeignKey(User,related_name='cliente_recibe_usuario_registro',on_delete=models.CASCADE)
	pais_pk = models.ForeignKey(Pais, blank=True, null=True,on_delete=models.CASCADE)
	departamento_pk = models.ForeignKey(Departamento, blank=True, null=True,on_delete=models.CASCADE)

	def __str__(self):
		return '{} | {}'.format(self.nombre_completo,self.celular)

class EstadoEnvio(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	estado = models.CharField(max_length=100, blank=False, null=False)
	def __str__(self):
		return '{} | {} '.format(self.empresa,self.estado)

class EmpresaControlCaja(models.Model):
	medida_caja = models.CharField(max_length=50, default='')
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	compra = models.IntegerField(default=0)
	existencia = models.IntegerField(default=0)
	recibo_no = models.CharField(max_length=50,default='')
	valor = models.FloatField()
	fecha = models.DateField(auto_now_add=True)
	recibo = models.FileField(upload_to="archivos_compra_cajas/", null=True, blank=True)
	usuario_registro = models.ForeignKey(User,related_name='empresa_caja_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{}'.format(self.medida_caja)

class EmpresaActividades(models.Model):
	empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	fecha = models.DateField()
	hora = models.CharField(max_length=50)
	descripcion_pedido = models.CharField(max_length=300,null=True)
	estado = models.BooleanField(default=False) #FALSE Pendiente / TRUE Realizado
	deposito = models.FloatField(default=0.00)
	cierre = models.BooleanField(default=False) #False pendiente / True Cerrado
	fecha_realizo = models.DateField(auto_now_add=True)
	fecha_cierre = models.DateField(auto_now_add=True)
	descripcion_entrega = models.CharField(max_length=300,null=True)
	actividad = models.BooleanField() #False es recoger / True es entregar
	recibo_entrega = models.CharField(max_length=10,blank=True, null=True)
	usuario_registro = models.ForeignKey(User,related_name='empresa_agenda_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {} | {} {}'.format(self.empresa,self.cliente,self.fecha,self.hora)

class TipoContenido(models.Model):
	tipo_contenido = models.CharField(max_length=100, blank=False, null=False)
	def __str__(self):
		return '{}'.format(self.tipo_contenido)

class TipoEnvio(models.Model):
	tipo_envio = models.CharField(max_length=100, blank=False, null=False)
	def __str__(self):
		return '{}'.format(self.tipo_envio)

class Camion(models.Model):
	descripcion = models.CharField(max_length=100, blank=False, null=False)
	placa = models.CharField(max_length=100, blank=False, null=False)
	estado = models.BooleanField(default=True)
	esta_en_transito = models.BooleanField(default=False)
	estado_envio = models.ForeignKey(EstadoEnvio, blank=True, null=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} => {}'.format(self.descripcion,self.placa)

class Contenedor(models.Model):
	codigo_original = models.CharField(max_length=100, blank=False, null=False)
	codigo_express = models.CharField(max_length=100, blank=False, null=False)
	pais_destino = models.ForeignKey(Pais,on_delete=models.CASCADE)
	pies_cubicos = models.FloatField(default=0.00)
	observacion =  models.CharField(max_length=100, blank=False, null=False)
	estado = models.ForeignKey(EstadoEnvio, blank=True, null=True,on_delete=models.CASCADE)
	fecha_ingreso_houston = models.DateTimeField(auto_now_add=True,blank=False, null=False)
	fecha_ingreso_puerto_houston = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	fecha_transito_maritimo = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	fecha_puerto_honduras = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	fecha_bodega_honduras = models.DateTimeField(auto_now_add=True, blank=False, null=False)

	def __str__(self):
		return '{}'.format(self.codigo_original)


class HistorialContenedor(models.Model):
	contenedor = models.ForeignKey(Contenedor, blank=True, null=True,on_delete=models.CASCADE)
	estado = models.ForeignKey(EstadoEnvio, blank=True, null=True,on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
	comentario = models.CharField(max_length=100, blank=False, null=False)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return '{} - {}'.format(self.contenedor,self.comentario)

class Envio(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	codigo = models.CharField(max_length=100, blank=True, null=True)
	fecha_recoleccion = models.DateTimeField(auto_now_add=True)
	fecha_envio = models.DateField(auto_now_add=True)
	valor_envio = models.FloatField(null=False)
	valor_adicional = models.FloatField(null=True)
	emplasticado = models.BooleanField(default=False) #FALSE NO LLEVA / TRUE SI LLEVA
	valor_emplasticado = models.FloatField()
	valor_seguro = models.FloatField(default=0.00)
	quien_envia = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	quien_recibe = models.ForeignKey(ClienteRecibe, blank=True, null=True,on_delete=models.CASCADE)
	quien_recibev = models.CharField(max_length=200, blank=False, null=False)
	direccion_registrar = models.CharField(max_length=500, blank=False, null=False)
	celular_registrar = models.CharField(max_length=50, blank=True, null=True)
	comentario = models.CharField(max_length=1000, blank=True, null=True)
	descripcion_embarque = models.CharField(max_length=1000, blank=True, null=True)
	total = models.FloatField(null=False,default=0.00)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)
	pais_destino = models.ForeignKey(Pais,on_delete=models.CASCADE)
	departamento_destino = models.ForeignKey(Departamento,on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to = 'paquetes/imagen/',verbose_name="Imagen del envio",default='paquetes/eehn.png')
	pago_recibido = models.FloatField()
	cancelado = models.BooleanField(default=False) #False factura esta activa / True factura cancelada
	credito = models.BooleanField(default=False) # FALSE CONTADO/TRUE CREDITO
	revendedor = models.BooleanField(default=False) # false hecho por EE / factura creada de un revendedor
	revendedor_registro = models.ForeignKey(Revendedor,blank=True,null=True,on_delete=models.CASCADE)
	guia_revendedor = models.CharField(max_length=100, blank=True, null=True)
	aprobado = models.BooleanField(default=True) # false no pasa a cierre / true revisada y lista para cierre
	tipo_contenido = models.ForeignKey(TipoContenido,blank=True,null=True,on_delete=models.CASCADE)
	tipo_envio = models.ForeignKey(TipoEnvio,blank=True,null=True,on_delete=models.CASCADE)
	saldo_pendiente = models.FloatField(default=0.00)
	ticket = models.BooleanField(default=False) # False sin imprimir /True impreso
	cierre = models.BooleanField(default=False) #False sin cierre / True Cerrado
	fecha_cierre = models.DateField(auto_now_add=True)
	usuario_aprobo = models.ForeignKey(User,blank=True,null=True,related_name="usuario_aprobo",on_delete=models.CASCADE)
	contenedor = models.ForeignKey(Contenedor,blank=True,null=True,on_delete=models.CASCADE)
	camion = models.ForeignKey(Camion,blank=True,null=True,on_delete=models.CASCADE)
	firma_cliente = models.ImageField(upload_to = 'cliente/firma/',verbose_name="Firma Cliente",default='paquetes/eehn.png',blank=True,null=True)
	estado_envio = models.ForeignKey(EstadoEnvio,blank=True,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{0} | {1} | {2} '.format(self.codigo,self.quien_envia,self.pais_destino.nombre)


class TipoCaja(models.Model):
	descripcion = models.CharField(max_length=100, blank=True, null=True)
	largo = models.FloatField(default=0.00)
	ancho = models.FloatField(default=0.00)
	alto = models.FloatField(default=0.00)
	espacio_cubico = models.FloatField(default=0.00)
	usuario_registro = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return '{0} | {1}'.format(self.descripcion,self.espacio_cubico)

class CajaPais(models.Model):
	pais = models.ForeignKey(Pais,blank=True,null=True,on_delete=models.CASCADE)
	tipo_caja = models.ForeignKey(TipoCaja,blank=True,null=True,on_delete=models.CASCADE)
	precio = models.FloatField(default=0.00)
	usuario_registro = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return '{0} | {1}'.format(self.pais,self.tipo_caja)

class DetalleEnvio(models.Model):
	envio = models.ForeignKey(Envio,blank=True,null=True,on_delete=models.CASCADE)
	tipo_caja = models.ForeignKey(CajaPais,blank=True,null=True,on_delete=models.CASCADE)
	precio = models.FloatField(default=0.00)
	cantidad = models.IntegerField(default=0)
	codigo_orden = models.IntegerField(default=0) #orden para saber caja 1 caja 2 de x guia
	codigo = models.CharField(max_length=100, blank=True, null=True)
	fue_enviada = models.BooleanField(default=False) #False sin subir en contenedir / True subida en contenedor
	total = models.FloatField(default=0.00)
	fue_subida_camion = models.BooleanField(default=False) #False sin subir en camion / True subida en camion

	def __str__(self):
		return '{0} | {1} | {2}'.format(self.envio,self.tipo_caja,self.fue_subida_camion)

class SeguimientoEnvio(models.Model):
	codigo_envio =  models.ForeignKey(Envio,on_delete=models.CASCADE)
	estado = models.ForeignKey(EstadoEnvio,on_delete=models.CASCADE)
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	fechahora = models.DateTimeField(auto_now_add=True)
	comentario = models.CharField(max_length=500, blank=True, null=True)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return '{0} | {1} | {2} '.format(self.codigo_envio,self.estado,self.fechahora)

class HistorialEnvio(models.Model):
	codigo_envio =  models.ForeignKey(Envio,on_delete=models.CASCADE)
	estado = models.ForeignKey(EstadoEnvio,on_delete=models.CASCADE)
	fechahora = models.DateTimeField(auto_now_add=True)
	comentario = models.CharField(max_length=500, blank=True, null=True)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return '{0} | {1} | {2} '.format(self.codigo_envio,self.estado,self.fechahora)

class EmpresaTipoGasto(models.Model):
	tipo_gasto =  models.CharField(max_length=50)
	empresa = models.ForeignKey(Empresa, null=True, blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {}'.format(self.tipo_gasto, self.empresa)

class EmpresaGasto(models.Model):
	tipo_gasto =  models.ForeignKey(EmpresaTipoGasto,on_delete=models.CASCADE)
	empresa = models.ForeignKey(Empresa, null=True, blank=True,on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	recibo = models.CharField(max_length=50)
	valor = models.FloatField()
	pdf = models.FileField(upload_to="archivos_gastos/", null=True, blank=True)
	descripcion = models.CharField(max_length=300, null=True)
	usuario_registro = models.ForeignKey(User,related_name='empresa_gasto_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{} | {}'.format(self.tipo_gasto, self.empresa)

class PagosCredito(models.Model):
	envio = models.ForeignKey(Envio,on_delete=models.CASCADE)
	pago = models.FloatField()
	saldo = models.FloatField()
	fecha = models.DateField(auto_now=True)
	tipo_pago = models.BooleanField(default=True) #False Deposito / True Efectivo
	cierre = models.BooleanField(default=False) #False pendiente / True Cerrado
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)
	fecha_cierre = models.DateField(auto_now_add=True)
	ubicacion = models.ForeignKey(UbicacionEmpleado,null=True, blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{0}'.format(self.envio)

class ReciboCaja(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	recibo_no = models.CharField(max_length=100, blank=True, null=True)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	size_caja = models.CharField(max_length=100, blank=True, null=True)
	valor_caja = models.FloatField()
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)
	descripcion_entrega = models.CharField(max_length=1000, blank=True, null=True)
	fecha = models.DateField(auto_now_add=True)
	cierre = models.BooleanField(default=False) #False sin cierre / True Cerrado
	fecha_cierre = models.DateField(auto_now_add=True)
	def __str__(self):
		return '{0} | {1}'.format(self.recibo_no,self.cliente)

class EmpresaDetalleCaja(models.Model):
	caja = models.ForeignKey(EmpresaControlCaja,on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	recibo_no = models.CharField(max_length=50,default='')
	valor = models.FloatField(default=0)
	fecha = models.DateField(auto_now_add=True)
	recibo = models.FileField(upload_to="archivos_compra_cajas/", null=True, blank=True)
	accion = models.BooleanField(default=True) #TRUE ENTREGADA/FALSE COMPRADO
	recibo_caja = models.ForeignKey(ReciboCaja, null=True, blank=True,on_delete=models.CASCADE)
	usuario_registro = models.ForeignKey(User,related_name='detalle_caja_usuario_registro',on_delete=models.CASCADE)
	def __str__(self):
		return '{}'.format(self.caja)	    

class ReciboContenedor(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	recibo_no = models.CharField(max_length=100, blank=True, null=True)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	num_pasaporte = models.CharField(max_length=255)
	correo = models.EmailField()
	telefono_adicional = models.CharField(max_length=15, blank=True, null=True)
	pais_destino = models.CharField(max_length=15, blank=True, null=True)
	puerto_destino = models.CharField(max_length=15, blank=True, null=True)
	nombre_recibe = models.CharField(max_length=255, blank=True, null=True)
	telefono_recibe = models.CharField(max_length=255, blank = True, null = True)
	nip_rtn = models.CharField(max_length=20, blank=True, null=True)
	tamano_contenedor = models.CharField(max_length=100, blank=True, null=True)
	valor_contenedor = models.FloatField()
	pdf = models.FileField(upload_to="archivos_pdf_contenedores/", null=True, blank=True)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
	cierre = models.BooleanField(default=False) #False sin cierre / True Cerrado
	fecha_cierre = models.DateField(auto_now_add=True)
	def __str__(self):
		return '{0}'.format(self.cliente)

class ReciboVehiculos(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True,on_delete=models.CASCADE)
	recibo_no = models.CharField(max_length=100, blank=True, null=True)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	num_pasaporte = models.CharField(max_length=255)
	correo = models.EmailField()
	telefono_adicional = models.CharField(max_length=15, blank=True, null=True)
	pais_destino = models.CharField(max_length=15, blank=True, null=True)
	puerto_destino = models.CharField(max_length=15, blank=True, null=True)
	nombre_recibe = models.CharField(max_length=255, blank=True, null=True)
	telefono_recibe = models.CharField(max_length=255, blank = True, null = True)
	nip_rtn = models.CharField(max_length=20, blank=True, null=True)
	marca_vehiculo = models.CharField(max_length=255, blank=True, null=True)
	modelo_vehiculo = models.CharField(max_length=255, blank=True, null=True)
	vin_vehiculo = models.CharField(max_length=255, blank=True, null=True)
	valor_vehiculo =  models.FloatField()
	observaciones = models.CharField(max_length=300, blank=True, null=True)
	pdf = models.FileField(upload_to="archivos_pdf_vehiculos/", null=True, blank=True)
	usuario_registro = models.ForeignKey(User,on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
	cierre = models.BooleanField(default=False) #False sin cierre / True Cerrado
	fecha_cierre = models.DateField(auto_now_add=True)
	prueba_dato = models.BooleanField(default=False)
	prueba_dato_1 = models.CharField(max_length=254, blank=True, null=True)

	def __str__(self):
		return '{0}'.format(self.cliente)

class TipoMensajes(models.Model):
	tipo_mensaje = models.CharField(max_length=50)
	
	def __str__(self):
		return '{0}'.format(self.tipo_mensaje)

class EmpresaMensaje(models.Model):
	tipo_mensaje = models.ForeignKey(TipoMensajes,on_delete=models.CASCADE)
	envio = models.ForeignKey(Envio, blank=True, null=True,on_delete=models.CASCADE)
	texto = models.CharField(max_length=1000)
	fecha = models.DateField(auto_now_add=True)
	precio = models.FloatField(default=0.25)
	pagado = models.BooleanField(default= False) #FALSE sin pagar / TRUE pagado
	fecha_pago = models.DateField(auto_now_add=True)

	def __str__(self):
		return '{} | {}'.format(self.tipo_mensaje, self.envio)

#KC MODELS
class SistemaEmpresa(models.Model):
    codigo_empresa = models.CharField(max_length=5)
    nombre_empresa = models.CharField(max_length=100)
    slogan_empresa = models.CharField(max_length=100)
    logo_empresa = models.CharField(max_length=100, blank=True, null=True)
    direccion_empresa = models.CharField(max_length=200)
    telefono_empresa = models.CharField(max_length=100)
    celular_empresa = models.CharField(max_length=100)
    correo_empressa = models.CharField(max_length=254)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sistema_empresa'

class SistemaPais(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sistema_pais'
        
class SistemaDepartamento(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey('SistemaPais', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sistema_departamento'

class SistemaEstado(models.Model):
    estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sistema_estado'

class SistemaRevendedor(models.Model):
    nombre_completo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono_empresa = models.CharField(max_length=100, blank=True, null=True)
    celular_empresa = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=254)
    logo = models.CharField(max_length=100, blank=True, null=True)
    es_revendedor = models.BooleanField()
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING,related_name="usuario_revendedor_kc")
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING,related_name="usuario_aprobo_revendedor_kc")

    class Meta:
        managed = False
        db_table = 'sistema_revendedor'

class SistemaCliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    correo = models.CharField(max_length=254, blank=True, null=True)
    revendedor = models.BooleanField()
    empresa = models.ForeignKey('SistemaEmpresa', models.DO_NOTHING)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING)
    revenedor_creo = models.ForeignKey('SistemaRevendedor', models.DO_NOTHING)
    estado = models.ForeignKey('SistemaEstado', models.DO_NOTHING, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'sistema_cliente'

class SistemaClienterecibe(models.Model):
    nombre_completo = models.CharField(max_length=100)
    celular = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    cliente_envia = models.ForeignKey(SistemaCliente, models.DO_NOTHING)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING)
    departamento = models.CharField(max_length=300, blank=True, null=True)
    pais = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_clienterecibe'

class SistemaEmpresaestadoenvio(models.Model):
    estado = models.CharField(max_length=100)
    empresa = models.ForeignKey(SistemaEmpresa, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sistema_empresaestadoenvio'

class SistemaTipocontenido(models.Model):
    tipo_contenido = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sistema_tipocontenido'

class SistemaTipoenvio(models.Model):
    tipo_envio = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sistema_tipoenvio'

class SistemaEmpresaenvio(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    fecha_recoleccion = models.DateTimeField()
    fecha_envio = models.DateField()
    descripcion_embarque = models.CharField(max_length=1000, blank=True, null=True)
    valor_envio = models.FloatField()
    valor_adicional = models.FloatField()
    valor_emplasticado = models.FloatField()
    total = models.FloatField()
    pago_recibido = models.FloatField()
    saldo_pendiente = models.FloatField()
    emplasticado = models.BooleanField()
    credito = models.BooleanField()
    comentario = models.CharField(max_length=1000, blank=True, null=True)
    ticket = models.BooleanField()
    cierre = models.BooleanField()
    cancelado = models.BooleanField()
    fecha_cierre = models.DateField()
    revendedor = models.BooleanField()
    guia_revendedor = models.CharField(max_length=100, blank=True, null=True)
    aprobado = models.BooleanField()
    empresa = models.ForeignKey(SistemaEmpresa, models.DO_NOTHING)
    departamento_destino = models.ForeignKey(SistemaDepartamento, models.DO_NOTHING)
    pais_destino = models.ForeignKey('SistemaPais', models.DO_NOTHING)
    quien_envia = models.ForeignKey(SistemaCliente, models.DO_NOTHING)
    quien_recibe = models.ForeignKey(SistemaClienterecibe, models.DO_NOTHING)
    usuario_aprobo = models.ForeignKey(AuthUser, models.DO_NOTHING)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING,related_name="usuario_aprobo_kc")
    direccion_registrar = models.CharField(max_length=1000, blank=True, null=True)
    celular_registrar = models.CharField(max_length=50, blank=True, null=True)
    valor_seguro = models.FloatField()
    tipo_contenido = models.ForeignKey('SistemaTipocontenido', models.DO_NOTHING, blank=True, null=True)
    tipo_envio = models.ForeignKey('SistemaTipoenvio', models.DO_NOTHING, blank=True, null=True)
    revendedor_registro = models.ForeignKey('SistemaRevendedor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_empresaenvio'

class SistemaHistorialenvio(models.Model):
    fechahora = models.DateTimeField()
    comentario = models.CharField(max_length=500, blank=True, null=True)
    codigo_envio = models.ForeignKey(SistemaEmpresaenvio, models.DO_NOTHING)
    estado = models.ForeignKey(SistemaEmpresaestadoenvio, models.DO_NOTHING)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sistema_historialenvio'

class SistemaSeguimientoenvio(models.Model):
    fechahora = models.DateTimeField()
    comentario = models.CharField(max_length=500, blank=True, null=True)
    codigo_envio = models.ForeignKey(SistemaEmpresaenvio, models.DO_NOTHING)
    estado = models.ForeignKey(SistemaEmpresaestadoenvio, models.DO_NOTHING)
    usuario_registro = models.ForeignKey(AuthUser, models.DO_NOTHING)
    empresa = models.ForeignKey(SistemaEmpresa, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_seguimientoenvio'

class SistemaTipomensajes(models.Model):
    tipo_mensaje = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sistema_tipomensajes'

class SistemaEmpresamensaje(models.Model):
    texto = models.CharField(max_length=1000)
    fecha = models.DateField()
    precio = models.FloatField()
    pagado = models.BooleanField()
    fecha_pago = models.DateField()
    envio = models.ForeignKey(SistemaEmpresaenvio, models.DO_NOTHING, blank=True, null=True)
    tipo_mensaje = models.ForeignKey(SistemaTipomensajes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sistema_empresamensaje'