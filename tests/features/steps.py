# -*- coding: utf-8 -*-
from lettuce import step

#1.- steps eliminar_prenda
@step(u'Given Que selecciono la prenda de “Juan Perez” en la lista de prendas')
def given_que_selecciono_la_prenda_de_juan_perez_en_la_lista_de_prendas(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de eliminar')
def when_oprimo_el_boton_de_eliminar(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver eliminada la prenda de “Juan Perez”.')
def then_puedo_ver_eliminada_la_prenda_de_juan_perez(step):
    assert False, 'This step must be implemented'

#2.- steps modificar_prenda
@step(u'Given Que selecciono la “Prenda de Juan Perez”')
def given_que_selecciono_la_prenda_de_juan_perez(step):
    assert False, 'This step must be implemented'
@step(u'When  Selecciono el botón “Editar”')
def when_selecciono_el_boton_editar(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver la prenda de “Juan Perez” en el formulario de pedido.')
def then_puedo_ver_la_prenda_de_juan_perez_en_el_formulario_de_pedido(step):
    assert False, 'This step must be implemented'

#3.- steps registrar_prenda
@step(u'Given Que selecciono el botón “Registrar Prenda” en el formulario nuevaPrenda')
def given_que_selecciono_el_boton_registrar_prenda_en_el_formulario_nuevaprenda(step):
    assert False, 'This step must be implemented'
@step(u'When ingreso los datos de la prenda')
def when_ingreso_los_datos_de_la_prenda(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el prenda en la lista de prendas (incluye propitario y costo).')
def then_puedo_ver_el_prenda_en_la_lista_de_prendas_incluye_propitario_y_costo(step):
    assert False, 'This step must be implemented'

#4.- steps registrar_empleado
@step(u'Given Que ingreso el empleado “Juan Perez” en la caja de Texto')
def given_que_ingreso_el_empleado_juan_perez_en_la_caja_de_texto(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de guardar')
def when_oprimo_el_boton_de_guardar(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el empleado “Juan Perez” en la lista de empleados registrados en el sistema')
def then_puedo_ver_el_empleado_juan_perez_en_la_lista_de_empleados_registrados_en_el_sistema(step):
    assert False, 'This step must be implemented'

#5.- steps modificar_empleado
@step(u'Given Que selecciono al empleado “Juan Perez” en la lista de empleados')
def given_que_selecciono_al_empleado_juan_perez_en_la_lista_de_empleados(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de “Editar”')
def when_oprimo_el_boton_de_editar(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el empleado “Juan Perez” en el formulario de empleado.')
def then_puedo_ver_el_empleado_juan_perez_en_el_formulario_de_empleado(step):
    assert False, 'This step must be implemented'

#6.- steps lista_de_empleados
@step(u'Given Que selecciono el menú empleados')
def given_que_selecciono_el_menu_empleados(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de “Empleados”')
def when_oprimo_el_boton_de_empleados(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver la lista completa de los empleados registrados en el sistema.')
def then_puedo_ver_la_lista_completa_de_los_empleados_registrados_en_el_sistema(step):
    assert False, 'This step must be implemented'

#7.- steps lista_de_clientes
@step(u'Given Que selecciono el menú clientes')
def given_que_selecciono_el_menu_clientes(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de “Prendas”')
def when_oprimo_el_boton_de_prendas(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver la lista completa de las prendas y con ello el nombre de los propietarios “clientes”.')
def then_puedo_ver_la_lista_completa_de_las_prendas_y_con_ello_el_nombre_de_los_propietarios_clientes(step):
    assert False, 'This step must be implemented'

#8.- steps ingresar_al_sistema
@step(u'Given me identifico como empleado/administrador')
def given_me_identifico_como_empleado_administrador(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de “Log-in”')
def when_oprimo_el_boton_de_log_in(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver la pantalla principal del sistema.')
def then_puedo_ver_la_pantalla_principal_del_sistema(step):
    assert False, 'This step must be implemented'
@step(u'Given me identifico como empleado')
def given_me_identifico_como_empleado(step):
    assert False, 'This step must be implemented'

#9.- steps eliminar_empleado
@step(u'Given Que selecciono el empleado “Juan Perez” en la lista de empleados')
def given_que_selecciono_el_empleado_juan_perez_en_la_lista_de_empleados(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón “Eliminar”')
def when_oprimo_el_boton_eliminar(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el empleado eliminado “Juan Perez” de la lista de empleados.')
def then_puedo_ver_el_empleado_eliminado_juan_perez_de_la_lista_de_empleados(step):
    assert False, 'This step must be implemented'

#10.- steps consulta_historial_empleado_administrador
@step(u'Given Que selecciono al empleado “Pepe Prado” en la lista de empleado')
def given_que_selecciono_al_empleado_pepe_prado_en_la_lista_de_empleado(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el botón de historial')
def when_oprimo_el_boton_de_historial(step):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el historial completo  del empleado “Pepe Prado”')
def then_puedo_ver_el_historial_completo_del_empleado_pepe_prado(step):
    assert False, 'This step must be implemented'

#11.- steps consulta_historial_empleado_empleado
@step(u'Given Que selecciono al empleado Jose en la lista de empleado')
def given_que_selecciono_al_empleado_jose_en_la_lista_de_empleado(step):
    assert False, 'This step must be implemented'
@step(u'When Oprimo el boton de "([^"]*)"')
def when_oprimo_el_boton_de_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Then Puedo ver el historial completo del empleado Jose.')
def then_puedo_ver_el_historial_completo_del_empleado_jose(step):
    assert False, 'This step must be implemented'

[1;37mFeature: Como empleado de la tintoreria                           [1;30m# consulta_historial_empleado_empleado.feature:2[0m
[1;37m  quiero consultar el historial de los empleados                  [1;30m# consulta_historial_empleado_empleado.feature:3[0m
[1;37m  para poder ver las actividades que realizan los empleados.      [1;30m# consulta_historial_empleado_empleado.feature:4[0m

[1;37m  Scenario: Historial del empleado Jose                           [1;30m# consulta_historial_empleado_empleado.feature:6[0m
[1;30m    Given Que selecciono al empleado Jose en la lista de empleado [1;30m# steps.py:119[0m
[A[0;31m    Given Que selecciono al empleado Jose en la lista de empleado [1;41;33m# steps.py:119[0m
[1;31m    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/dist-packages/lettuce/core.py", line 144, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/vagrant/proyecto_final/tests/features/steps.py", line 120, in given_que_selecciono_al_empleado_jose_en_la_lista_de_empleado
        assert False, 'This step must be implemented'
    AssertionError: This step must be implemented[0m
[1;30m    When Oprimo el boton de "historial"                           [1;30m# steps.py:122[0m
[A[0;36m    When Oprimo el boton de "historial"                           [1;30m# steps.py:122[0m
[1;30m    Then Puedo ver el historial completo del empleado Jose.       [1;30m# steps.py:125[0m
[A[0;36m    Then Puedo ver el historial completo del empleado Jose.       [1;30m# steps.py:125[0m

[1;37m1 feature ([0;31m0 passed[1;37m)[0m
[1;37m1 scenario ([0;31m0 passed[1;37m)[0m
[1;37m3 steps ([0;31m1 failed[1;37m, [0;36m2 skipped[1;37m, [1;32m0 passed[1;37m)[0m

[1;31mList of failed scenarios:
[0;31m  Scenario: Historial del empleado Jose                           # consulta_historial_empleado_empleado.feature:6
[0m
