Feature: Como empleado/administrador de la Tintorería
		quiero obtener la lista de  clientes (en base a las prendas registradas)	
		para poder ver la lista de clientes (en base a las prendas registradas).

Scenario: Obtener Lista de Clientes
		Given Que selecciono el menú clientes
		When Oprimo el botón de “Prendas”
		Then Puedo ver la lista completa de las prendas y con ello el nombre de los propietarios “clientes”.