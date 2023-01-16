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
        for num in range(1,n+1):
            lis.append(num)
        #print(lis)
        print('\n')
        for num in lis:
            prim=True
            if num % 2 == 0:
                prim=False
            if prim:
                print(num,' no es multiplo de 2')
            else:
                print(num,' es multiplo de 2')
    elif opc=='C':
        n=int(input('Ingrese cantidad de usuarios: '))
        ##Creo lista general
        usuarios=[]
        for item in range(1, n+1):
            #Lista por usuario
            u=[]
            x = input(f'Ingrese el nombre del {item} usuario: ')
            y = int(input(f'Ingrese la edad del {item} usuario: ')) 
            u.append(x)
            u.append(y)
            usuarios.append(u)
            pass
        ##Mayores de edad
        print('\nUsuarios mayore de edad: ')
        for user in usuarios:
            if user[-1]>=18:
                print('\nNombre: ',user[0])
                print('Edad: ',user[-1])
            
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')