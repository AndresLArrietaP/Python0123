valor= int(input("\nValor a multiplicar: "))
lim = int(input("\n¿Cuantas veces multiplicar? "))

def multi(valor : int ,repe : int =1  ):
    if repe <=lim:
        repe+=1
        print(valor)
        return multi(valor*2,repe)
    else:
        print('Resultado: ',valor)
        print('\nFin')
multi(valor)