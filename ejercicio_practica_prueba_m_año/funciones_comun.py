#funciones que más estamos ocupando

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
        


        