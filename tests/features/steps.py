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