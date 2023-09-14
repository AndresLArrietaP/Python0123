##Pregunta 3

##Realizar una función que pase un entero por valor y lo multiplique por 2 y otra función
def mu():
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
            
    nameFile()   
    valor= int(input("\nValor a multiplicar: "))
    lim = int(input("\n¿Cuantas veces multiplicar por 2? "))
    multi(valor,lim)
    
def multi(valor : int ,lim: int,repe : int =1  ):
    if repe <=lim:
        repe+=1
        print(valor)
        return multi(valor*2,lim,repe)
    else:
        print('Resultado: ',valor)
        print('\nFin')
#mu()
#multi(valor)