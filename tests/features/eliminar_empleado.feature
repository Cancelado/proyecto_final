Feature: Como administrador de la Tintorería
		quiero eliminar empleados	
		para poder borrarlos de la lista de empleados.

Scenario: Dar de baja el empleado Juan Perez
		Given Que selecciono el empleado “Juan Perez” en la lista de empleados
		When Oprimo el botón “Eliminar”
		Then Puedo ver el empleado eliminado “Juan Perez” de la lista de empleados.