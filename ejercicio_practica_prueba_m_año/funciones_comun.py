#funciones que más estamos ocupando
import os
import numpy
import msvcrt
restaurant=numpy.zeros((3.3),int)


#crear arreglo y como acomodar a gusto
def ver_mesas ():
    for x in range(3):
        for y in range(3):
            print(restaurant[x][y], end=" ")
        print()


def rut_validar(rut):
    while True:
        try:
            rut=int(input("ingrese su rut sin puntos "-" y digito verificarod "))
            if rut>=1000000 and rut<=99999999:
                print("validado")
                return rut
            else:
                print("ERROR de datos")
        except:
            print("ERROR rut ingresado no valido")
            
def opc_carta (menu_carta):            
     print(f'''
                        carta de la casa
                    _________________________
                    1) Bibidas (tamaños de cada bebible consulte con el mesero en turno)
                    1_cerveza
                    2_jugo
                    3_Café
                    _____________________
                    2) Platos by Juan
                    1_Ensalada de mariscos
                    2_Ramén
                    3_Pique macho
                    _______________________
                    3) Postres
                    1_helado
                    2_yogurt
                    3_Flan especial de la casa
                        ''')
     
     
def validacion_carta (menu_carta):
    while True:
        try:
            menu_carta=int(input("Ingrese opcion deseada"))
            if menu_carta in(1,2,3):
                return menu_carta
            else:
                print("ERROR ingrese un número valido")
        except:
            print("ERROR ingrese un nro entero") 

            
def mostrar_menu ():
    print('''
                \t Menú 
                1_ver
                2_Reserva
                3_Carte
                4_Pagar
                5_cancelar
                6_cierre''')

def validar_opciones_menu (menu_ops_P):
     while True:
        try:
            menu_ops_P=int(input("Ingrese opcion deseada"))
            if menu_ops_P in(1,2,3,4,5,6):
                return menu_ops_P
            else:
                print("ERROR ingrese un número valido")
        except:
            print("ERROR ingrese un nro entero")            
                
def validar_nombre (P_nombre):
    while True:
        P_nombre=input("ingrese Nombre")
        if len(P_nombre.strip()) >= 3 and P_nombre.isalpha:
            print("datos aceptados")
            return P_nombre
        else:
            print("intente nuevamente")
        
def validar_correo(correo):
    while True:
        correo=input("ingrese correo")
        if "@" in (correo):
            return correo
        else:
            print("datos invalidos")
            
def rut_located(posicion,Ruts,rut):
    if rut in range(len(Ruts)):
            for x in range(len(Ruts)):
                if rut==Ruts[x]:
                    posicion=x
                    break
            return posicion
        


        