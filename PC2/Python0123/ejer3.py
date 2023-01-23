##Pregunta 3

##Definir una función que retorne el mayor valor al ingresar 2 números



#Se define
def compara(n1, n2):
    if n1>n2:
        return n1
    elif n1<n2:
        return n2
    else:
        print('\nSon iguales')
#Se pide
x=int(input('Primer número: '))
y=int(input('Segundo número: '))

r=compara(x,y)
print('\n')
print(r)