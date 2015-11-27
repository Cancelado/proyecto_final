Feature: Como administrador de la Tintorería
		quiero obtener la lista de  empleados	
		para poder ver la lista de empleados.

Scenario: Obtener Lista de Empleados
		Given Que selecciono el menú empleados
		When Oprimo el botón de “Empleados”
		Then Puedo ver la lista completa de los empleados registrados en el sistema.