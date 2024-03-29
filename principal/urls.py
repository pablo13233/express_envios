from django.conf.urls import url
from principal.views import *

urlpatterns = [
    url(r'^$', inicio_cliente, name='inicio_cliente'),
    url(r'^rastrear/encomienda/$', buscar_envio_cliente, name='buscar_envio_cliente'),
    url(r'^buscar/envio/$', buscar_envio, name='buscar_envio'),
    url(r'^resultado/busqueda/$', resultado_busqueda, name='resultado_busqueda'),
    url(r'^login/$', login, name='login'),
    url(r'^salir/$', cerrar_sesion, name='cerrar_sesion'),
    url(r'^contrasena/$', editarpass, name='editarpass'),
    url(r'^administracion/$', inicio_admin, name='inicio_admin'),
    url(r'^empresa/$', empresa, name='empresa'),
    url(r'^empleados/$', empleados, name='empleados'),
    url(r'^desactivar/usuario/(?P<id>\d+)/$', desactivar_usuario, name='desactivar_usuario'),
    url(r'^activar/usuario/(?P<id>\d+)/$', activar_usuario, name='activar_usuario'),
    url(r'^tipo/gasto$', tipo_gasto, name='tipo_gasto'),
    url(r'^gastos$', gastos, name='gastos'),
    url(r'^gasto/recibo/(?P<id>\d+)$', ver_recibo_gastos, name='ver_recibo_gastos'),
    url(r'^cajas$', cajas, name='cajas'),
    url(r'^detalle/compra/(?P<id>\d+)$', detalle_compra_cajas, name='detalle_compra_cajas'),
    url(r'^detalle/recibo/(?P<id>\d+)$', ver_detalle_recibos_cajas, name='ver_detalle_recibos_cajas'),
    url(r'^caja/recibo/(?P<id>\d+)$', ver_recibos_cajas, name='ver_recibos_cajas'),
    url(r'^detalle/cajas$', detalle_cajas, name='detalle_cajas'),
    url(r'^actividades$', actividades, name='actividades'),
    url(r'^finalizar/actividad$', finalizar_actividad, name='finalizar_actividad'),
	url(r'^recibo/caja/(?P<id>\d+)/$', recibo_caja_pdf, name='recibo_caja_pdf'),
	url(r'^terminar/tarea/$', terminar_tarea, name='terminar_tarea'),
	url(r'^reactivar/tarea/$', reactivar_tarea, name='reactivar_tarea'),
    url(r'^clientes$', clientes, name='clientes'),
    url(r'^recibe$', recibe, name='recibe'),
    url(r'^ver$', ver_recibe, name='ver_recibe'),
    url(r'^datos$', datos_recibe, name='datos_recibe'),
    url(r'^departamentos/$', departamento, name='departamento'),
	url(r'^municipios/$', municipio, name='municipio'),
    url(r'^registrar/envio/$', registrar_envio, name='registrar_envio'),
    url(r'^envio/pdf/(?P<id>\d+)/$', envio_pdf, name='envio_pdf'),
    url(r'^ver/paquetes/(?P<id_estado>\d+)/$', ver_paquetes, name='ver_paquetes'),
    url(r'^traslado/post/$', trasladar_post, name='trasladar_post'),
    ##MODULO REVENDEDOR
    url(r'^revendedor$', revendedor, name='revendedor'),
	url(r'^desactivar/usuario(?P<id>\d+)/$', desactivar_usuario, name='desactivar_usuario'),
    url(r'^activar/usuario(?P<id>\d+)/$', activar_usuario, name='activar_usuario'),
	url(r'^aprobar/envios$', aprobar_envios, name='aprobar_envios'),
	url(r'^aprobar/post$', aprobar_post, name='aprobar_post'),
    ##
    url(r'^creditos/$', envios_credito, name='envios_credito'),
    url(r'^impresion/tickets/$', tickets_envio, name='tickets_envio'),
	url(r'^imprimir/ticket/(?P<id>\d+)/$', imprimir_ticket, name='imprimir_ticket'),
	url(r'^cerrar/ticket/$', cerrar_ticket, name='cerrar_ticket'),
	url(r'^pago/envio/(?P<id>\d+)/$', pago_envio, name='pago_envio'),
    url(r'^impresion/creditos/$', imprimir_credito, name='imprimir_credito'),
	url(r'^cierre/$', cierre, name='cierre'),
	url(r'^realizar/cierre/$', realizar_cierre, name='realizar_cierre'),
    url(r'^ver/cierres/$', cierre_mensual, name='cierre_mensual'),
	url(r'^cierre/imprimir/$', cierre_mensual_print, name='cierre_mensual_print'),
	url(r'^cierre/diario/imprimir/$', cierre_diario_print, name='cierre_diario_print'),
    ##NUEVAS URL RECIBOS############
	url(r'^recibo/contenedor/$', recibo_contenedor, name='recibo_contenedor'),
	url(r'^recibo/contenedor/(?P<id>\d+)/$', recibo_contenedor_pdf, name='recibo_contenedor_pdf'),
	url(r'^ver/pdf/contenedor/(?P<id>\d+)/$', ver_pdf_contenedor_pdf, name='ver_pdf_contenedor_pdf'),
	url(r'^recibo/vehiculo/$', recibo_vehiculo, name='recibo_vehiculo'),
	url(r'^recibo/vehiculo/(?P<id>\d+)/$', recibo_vehiculo_pdf, name='recibo_vehiculo_pdf'),
	url(r'^ver/pdf/vehiculo/(?P<id>\d+)/$', ver_pdf_vehiculo_pdf, name='ver_pdf_vehiculo_pdf'),
    url(r'^top/clientes$', top_clientes, name='top_clientes'),

    url(r'^cajas/$', cajas_tipo, name='cajas_tipo'),
    url(r'^modal/recibe/$', modal_agregar_recibe, name='modal_agregar_recibe'),
    url(r'^modal/editar/recibe/$', modal_editar_recibe, name='modal_editar_recibe'),
    url(r'^modal/tipo/caja/$', modal_agregar_tipo_caja, name='modal_agregar_tipo_caja'),
    url(r'^modal/tipo/caja/editar/$', modal_editar_tipo_caja, name='modal_editar_tipo_caja'),
    url(r'^enviar/contenedor/$', cargar_contenedor, name='cargar_contenedor'),
    url(r'^ver/contenedor/(?P<id>\d+)/$', ver_contenedor_enviar, name='ver_contenedor_enviar'),
    url(r'^trasladar/contenedor/$', trasladar_contenedor, name='trasladar_contenedor'),
    url(r'^guias/faltante/(?P<id_contenedor>\d+)/$', lista_guias_faltante, name='lista_guias_faltante'),
    url(r'^reversion/guia/(?P<id_envio>\d+)/(?P<guia_hija>\w+)/$', trasladar_guia, name='trasladar_guia'),
    url(r'^guia/buscar/$', buscar_guia, name='buscar_guia'),
    url(r'^trasladar/caja/transito/$', enviar_transito, name='enviar_transito'),
    url(r'^trasladar/transito/(?P<envio>\w+)/$', trasladar_a_transito, name='trasladar_a_transito'),
    url(r'^buscar/caja/entrega/$', buscar_caja_transito, name='buscar_caja_transito'),
    url(r'^entregar/caja/(?P<envio>\w+)/$', entregar_caja, name='entregar_caja'),
    url(r'^reporte/ventas/$', reporte_ventas, name='reporte_ventas'),
    url(r'^distribuir/camion/$', seleccionar_camion, name='seleccionar_camion'),
    url(r'^ver/camion/(?P<id>\d+)/$', ver_camion_enviar, name='ver_camion_enviar'),
    url(r'^trasladar/camion/$', trasladar_camion, name='trasladar_camion'),
    url(r'^ver/faltante/camion/(?P<id_camion>\d+)/$', lista_guias_faltante_camion, name='lista_guias_faltante_camion'),
    url(r'^lista/camiones/$', camiones, name='camiones'),
    url(r'^activar/camion/(?P<id>\d+)/$', activar_camion, name='activar_camion'),
    url(r'^desactivar/camion/(?P<id>\d+)/$', desactivar_camion, name='desactivar_camion'),
    url(r'^datos/caja/edit/$', datos_caja_edit, name='datos_caja_edit'),
    url(r'^consultar/abonos/$', reporte_abonos, name='reporte_abonos'),
    # alksdalk
    url(r'^distribuir_cajas/', distribuir_cajas, name='distribuir_cajas'),
    url(r'^cajas_camion/(?P<id>\d+)/$', ver_cajas_camion, name='cajas_camion'),
    url(r'^recibir_bodega_hn/', recibir_bodega, name='recibir_bodega_hn'),
    url(r'^ver_recibido_bodega_hn/', recibido_bodega_hn, name='recibido_bodega_hn'),
    url(r'^ver/cierre_anual/$', cierre_anual, name='cierre_anual'),
	url(r'^cierre/anual/imprimir/$', cierre_anual_print, name='cierre_anual_print'),
    url(r'^registrar/envio-rv/$', registrar_envio_rv, name='registrar_envio_rv'),
    url(r'^reporte/cajas-contenedor/(?P<id>\d+)/$', cajas_contenedor_pdf, name='cajas_contenedor'),
    url(r'^cajas_a_bodega/$', busqueda_caja_bodega, name='cajas_a_bodega'),
    url(r'^cajas_caja_bodega/$', cargar_caja_camion, name='cargar_caja_camion'),
    url(r'^reporte/cajas-contenedor-xls/(?P<id>\d+)/$', cajas_contenedor_xls, name='cajas_contenedor_xls'),
    url(r'^reporte/estado-cajas-contenedor/(?P<id>\d+)/$', estado_cajas_contenedor_pdf, name='estado_cajas_contenedor'),
    url(r'^reporte/reversion-estado-honduras/$', reversion_estado_honduras, name='reversion_estado_honduras'),
    url(r'^reversion/guia-hn/$', trasladar_guia_hn, name='trasladar_guia_hn'),
    url(r'^faltantes/bodega-hn/$', lista_guias_faltante_bodega_hn, name='lista_faltante_bodega_hn'),
    url(r'^modal/editar/cliente/$', editar_dato_cliente, name='editar_dato_cliente'),
    url(r'^ajax/cliente/$', obtener_clientes_ajax, name='obtener_clientes_ajax'),
    url(r'^reportes/envios_rango_fecha_print/$', envios_rango_fecha_print, name='envios_rango_fecha_print'),
    url(r'^reporte/recibos-envios-contenedor/(?P<id>\d+)/$', generar_recibos_por_contenedor, name='recibos_por_contenedor'),
    
    
]
# url(r'^$', inicio, name='inicio'),
# url(r'^servicios/$', servicios, name='servicios'),
# url(r'^ver/pdf/vehiculo/(?P<id>\d+)/$', ver_pdf_vehiculo_pdf, name='ver_pdf_vehiculo_pdf'),
