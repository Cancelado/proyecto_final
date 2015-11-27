Feature: Como administrador de la Tintorería
		quiero consultar el historial de los empleados	
		para poder ver las actividades que realizan los empleados.

Scenario: Historial del empleado “Pepe Prado”
		Given Que selecciono al empleado “Pepe Prado” en la lista de empleado
		When Oprimo el botón de historial
		Then Puedo ver el historial completo  del empleado “Pepe Prado”