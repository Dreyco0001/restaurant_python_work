#ejercicio test prueba
#recordar IVA 19%
#menu con opciones 1_ver /2_reserva/3_carta/4_pagar/5_calcelar/6_salir
#---------------------------------------
import numpy as np
import funciones_comun as fc    
from funciones_comun import *
#---------------------------------------

#carta
#bebidas
cerveza=2500
jugo=1000
cafe=1500

#platos
ensalada_mariscos=7000
Ramen=4000
pique_macho=3500

#postres
helado=1000
yogurt=500
flan_especial=2000

#ventas
subtotal=0
IVA=0
Descuento=0
total=0



#arreglos y listas





while True:
    print("welcome a pollos hermanos Restaurant.")
    fc.mostrar_menu()
    menu_ops_P = fc.validar_opciones_menu()
    if menu_ops_P==1:#ver mesas libres
        fc.ver_mesas()
        
    elif menu_ops_P==2:#ver reserva
        pass
    elif menu_ops_P==3:#carta
        rut=rut_validar()
        if rut in Ruts:
            posicion=rut_located
        else:
            print("proceso de pago de mesa activado")
            continue
        fc.opc_carta()
        
        menu_carta=fc.validacion_carta()
        
        
        
    elif menu_ops_P==4:#pagar
        rut=rut_validar()
        if rut in Ruts:
            print("proceso de pago de mesa activado")
            posicion=rut_located
        else:
            continue
            
    elif menu_ops_P==5:#cancelar
        rut=rut_validar()
        if rut in Ruts:
            continue
        else:
            print("Calcelar reserva")
            posicion=rut_located
            
    else:#Cierre sistema
            while True:
                try:
                    cierre=int(input("¿Seguro que quiere cerrar?(si=1/no=2) _"))
                    if cierre in(1,2):
                        break
                    else:
                        print("opcion invalida")
                except:
                    print("ERROR de datos ingrese nro entero")
            if cierre==1:
                break
            elif cierre==2:
                continue