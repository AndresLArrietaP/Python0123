##Pregunta 6

#Imprima el nombre del archivo en ejecución

def dir():
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
            
    nameFile()   
    
    import sys
    variable =sys.argv[0]
    print("\n")
    print('Esta es: ',variable)
#dir()