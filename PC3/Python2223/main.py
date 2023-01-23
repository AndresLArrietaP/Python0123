##Pregunta 1

##En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás problemas.

from ejer5 import *
class main:
    def nameFile():
        if __name__=='__main__':
            print("APP")
        else:
            print("SECUNDARIO")
main.nameFile()