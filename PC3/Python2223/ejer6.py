##Pregunta 6

#Imprima el nombre del archivo en ejecución

def dir():
    import sys
    variable =sys.argv[0]
    print("\n")
    print('Esta es: ',variable)
#dir()