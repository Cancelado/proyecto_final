
Feature: Como empleado o administrador de la Tintorería
    quiero eliminar prendas
    para poder borrarlos de la lista de prendas.

Scenario: Dar de baja la prenda de Juan Perez
    Given Que selecciono la prenda de “Juan Perez” en la lista de prendas
    When Oprimo el botón de eliminar
    Then Puedo ver eliminada la prenda de “Juan Perez”.