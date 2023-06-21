#funciones que más estamos ocupando
import os
import numpy
import msvcrt
import time
#arreglos 
restaurant=numpy.zeros((3,3),int)
Ruts_lista=[]
P_nombres_lista=[]
correo_lista=[]
fila_lista=[]
colupna_lista=[]
Ruts=[]
rut={}
pago=[]
menu_carta=0
menu_carta1=0

#crear arreglo y como acomodar a gusto
def ver_mesas ():
    for x in range(3):
        print(f"personas {(x+1)*2} ")
        for y in range(3):
            print(restaurant[x][y], end=" ")
        print()
    msvcrt.getch()


def rut_validar():
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
                    _____________________
                    2) Platos by Juan
                    _______________________
                    3) Postres
                    _________________________
                    4)pagar
                    _______________________
                    5)cancelar
                        ''')
     
     
def validacion_carta ():
    while True:
        try:
            menu_carta=int(input("Ingrese opcion deseada"))
            if menu_carta in(1,2,3,4,5):
                return menu_carta
            else:
                print("ERROR ingrese un número valido")
        except:
            print("ERROR ingrese un nro entero") 

def validacion_carta1 ():
    while True:
        try:
            menu_carta=int(input("Ingrese opcion deseada"))
            if menu_carta in(1,2,3):
                return menu_carta
            else:
                print("ERROR ingrese un número valido")
        except:
            print("ERROR ingrese un nro entero") 

def opciones_carta():
    if menu_carta==1:
        print('''
            1_cerveza $2500
            2_jugo    $1000
            3_Café    $1500''')
        
    elif menu_carta==2:
        print('''
                1_Ensalada de mariscos $7000
                2_Ramén $4000
                3_Pique macho $3500
              ''')
        
        
    elif menu_carta==3:
        
        print('''
            1_helado  $1000
            2_yogurt $500
            3_Flan especial de la casa  $2000
              ''')
    elif menu_carta==4:
        
    else:
            
def mostrar_menu ():
    print('''
                \t Menú 
                1_ver
                2_Reserva
                3_Carte
                4_Pagar
                5_cancelar
                6_cierre''')

def validar_opciones_menu ():
     while True:
        try:
            menu_ops_P=int(input("Ingrese opcion deseada"))
            if menu_ops_P in(1,2,3,4,5,6):
                return menu_ops_P
            else:
                print("ERROR ingrese un número valido")
        except:
            print("ERROR ingrese un nro entero")            
                
def validar_nombre ():
    while True:
        P_nombre=input("ingrese Nombre")
        if len(P_nombre.strip()) >= 3 and P_nombre.isalpha:
            print("datos aceptados")
            return P_nombre
        else:
            print("intente nuevamente")
        
def validar_correo():
    while True:
        correo=input("ingrese correo")
        if "@" in (correo):
            return correo
        else:
            print("datos invalidos")
            
def rut_located():
    if rut in range(len(Ruts)):
            for x in range(len(Ruts)):
                if rut==Ruts[x]:
                    posicion=x
                    break
            return posicion
        

        
def crear_usr():
    CORREO=validar_correo
    NOMBRE=validar_nombre
    RUT=rut_validar
    correo_lista.append(CORREO)
    Ruts_lista.append(RUT)
    P_nombres_lista=(NOMBRE)
    
    
    