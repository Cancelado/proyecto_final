Feature: Como empleado/administrador de la Tintorería
		quiero ingresar al sistema	
		para poder administrar el sistema.

Scenario: Log-in administrador
		Given me identifico como empleado/administrador
		When Oprimo el botón de “Log-in”
		Then Puedo ver la pantalla principal del sistema.

Scenario: Log-in empleado
		Given me identifico como empleado
		When Oprimo el botón de “Log-in”
		Then Puedo ver la pantalla principal del sistema.