##Pregunta 1

##Realizar un Menú Iterativo que tenga las siguientes opciones
#- Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
#- Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número
#- Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
##Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]

msg = """\nElija una de las siguientes opciones:

a) Dibujar un cuadrado con *.
b) Iteración de una lista de números IDENTIFICANDO si es múltiplo de 2 (imprime el número).
c) Iteración de una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.

"""
##inputs

print(msg)

opc=input('Ingresar la opción: ').upper()

print('Opción elegida: ',opc)

if(opc!='A' or opc!='B' or opc!='C'):
    if opc=='A':
        h = int(input('Ingrese la medida del lado del cuadrado: '))
        for i in range(h):
            f = i+1 # valor fila
            print('*'* (h))
    elif opc=='B':
        n=int(input('Ingrese cantidad de números: '))
        ##Creo lista
        lis=[]
        for i,num in enumerate(lis):

            print('a')
    elif opc=='C':
        print('a')
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')