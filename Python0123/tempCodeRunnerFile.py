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
        print('a')
    elif opc=='C':
        print('a')
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')