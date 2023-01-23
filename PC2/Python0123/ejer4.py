##Pregunta 4

##Definir una función que imprima los argumentos ingresados desde línea de comandos
#Nota: Usar  import sys.argv => *args

#Se define
import sys

def arg(*args):
    for arg in args:
        print(arg)

arg(sys.argv)