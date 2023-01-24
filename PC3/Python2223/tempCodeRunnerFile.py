##Pregunta 1

##En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás problemas.
import os 
from ejer2 import *
from ejer3 import *
from ejer4 import *
from ejer5 import *
from ejer6 import *
from ejer7 import *
class main:
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
main.nameFile()


msg = """\n________PRÁCTICA 3________
    
    ELIJA EL EJERCICIO:

    a) Ejer. 2
    b) Ejer. 3
    c) Ejer. 4
    d) Ejer. 5
    e) Ejer. 6
    f) Ejer. 7

    """

print(msg)

opc=input('Ingresar la opción: ').upper()
print('Opción elegida: ',opc)

if(opc!='A' or opc!='B' or opc!='C'or opc!='D'or opc!='E'or opc!='F'):
    if opc=='A':
        texto()
    elif opc=='B':
        mu()
    elif opc=='C':
        tienda()
    elif opc=='D':
        try:
            print('\n<<<SUMA>>>\n')
            sumydiv()
        except:
            print("Ha ocurrido un error en alguna función")
        else:
            print("\nDirectorio")
            print(os.getcwd())
        finally:
            print("\nProceso terminado") 
    elif opc=='E':
        dir()
    elif opc=='F':
        codprod()
    else:
        print('OPCION INVÁLIDA')
else:
    print('OPCIÓN INVALIDA')
