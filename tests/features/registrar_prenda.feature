Feature: Como empleado/administrador de la Tintorería
		quiero registrar prenda	
		para poder modificar la lista de pedidos.

Scenario: Registrar prenda “Registrando Prenda de Juan Perez”
		Given Que selecciono el botón “Registrar Prenda” en el formulario nuevaPrenda
		When ingreso los datos de la prenda
		Then Puedo ver el prenda en la lista de prendas (incluye propitario y costo).