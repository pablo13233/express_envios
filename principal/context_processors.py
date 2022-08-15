from .models import *

def get_empleado(request):
	if request.user.is_authenticated:
		empleado = Empleado.objects.get(usuario=request.user)
		print empleado,'contex processor'
		return {'get_empleado': empleado}
	else:
		return {'get_empleado': None}