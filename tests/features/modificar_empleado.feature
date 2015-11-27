Feature: Como administrador de la Tintorería
		quiero modificar empleados	
		para poder modificar de la lista de empleados actualizada.

Scenario: Modificar el empleado Juan Perez
		Given Que selecciono al empleado “Juan Perez” en la lista de empleados
		When Oprimo el botón de “Editar”
		Then Puedo ver el empleado “Juan Perez” en el formulario de empleado.