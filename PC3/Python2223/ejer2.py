##Pregunta 2

##Realizar un programa que realice las siguientes funciones de string al texto.
#-split
#-join
#-count
#-find
#-uppercase
#-lowercase

def texto():
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
            
    nameFile()     
    texto="""LoremIpsum es simplemente el texto de relleno de las imprentas y archivos de texto.
    LoremIpsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
    impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
    y los mezcló de tal manera que logró hacer un libro de textos especimen."""

    msg = """\nElija una de las siguientes operaciones:

    a) F.Split
    b) F.Join
    c) F.Count
    d) F.Find
    e) F.Uppercase
    f) F.Lowercase

    """
    msgsplit = """\nElija con o sin delimitador:

    a) F.Split libre
    b) F.Split con límite

    """

    print(msg)

    opc=input('Ingresar la opción: ').upper()
    print('Opción elegida: ',opc)

    if(opc!='A' or opc!='B' or opc!='C'or opc!='D'or opc!='E'or opc!='F'):
        if opc=='A':
            print(msgsplit)
            opc2=input('\nIngresar la opción: ').upper()
            if opc2=='A':
                print(texto.split(sep=" "))
            elif opc2=='B':
                lim=int(input('\nIngresar límite: '))
                print(texto.split(sep=" ", maxsplit=lim))
            else:
                print('OPCION INVÁLIDA')  
        elif opc=='B':
            #separación previa
            print('\nAntes de unir')
            lista=texto.split(sep=" ")
            print(lista)
            #unión
            print('\nUnido')
            print(" ".join(lista))
        elif opc=='C':
            w=input('\nIngresar palabra a contar: ')
            print(texto.count(w))
        elif opc=='D':
            w2=input('\nIngresar palabra a buscar: ')
            print(texto.find(w2))
        elif opc=='E':
            print(texto.upper())
        elif opc=='F':
            print(texto.lower())
        else:
            print('OPCION INVÁLIDA')
    else:
        print('OPCIÓN INVALIDA')

#texto()