
Feature: Como empleado de la tintoreria
		quiero consultar el historial de los empleados	
		para poder ver las actividades que realizan los empleados.

Scenario: Historial del empleado Jose
		Given Que selecciono al empleado Jose en la lista de empleado
		When Oprimo el boton de "historial"
		Then Puedo ver el historial completo del empleado Jose.