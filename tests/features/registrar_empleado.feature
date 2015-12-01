Feature: Como administrador de la tintoreria
		quiero registrar empleados	
		para poder incorporarlos a tintoreria.

Scenario: Dar de alta el empleado Juan Perez
		Given Que ingreso el empleado “Juan Perez” en la caja de Texto
		When Oprimo el botón de guardar
		Then Puedo ver el empleado “Juan Perez” en la lista de empleados registrados en el sistema