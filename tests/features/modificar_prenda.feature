Feature: Como empleado/administrador de la Tintorería
		quiero modificar una prenda	
		para poder modificar las características de la prenda.

Scenario: Modificar prenda “Prenda de Juan Perez”
		Given Que selecciono la “Prenda de Juan Perez”
		When  Selecciono el botón “Editar”
		Then Puedo ver la prenda de “Juan Perez” en el formulario de pedido.