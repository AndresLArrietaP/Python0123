def compara(n1, n2):
    if n1>n2:
        return n1
    elif n1<n2:
        return n2
    else:
        print('\nIguales')
#Se pide
x=int(input('Primer número: '))
y=int(input('Segundo número: '))

r=compara(x,y)
print('\n')
print(r)