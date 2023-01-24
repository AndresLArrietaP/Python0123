##Pregunta 7

#Programa que tenga una clase Producto el cual solo tiene el atributo de nombre ,codigo
#el cual tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un
#método que permita imprimir el objeto de forma literal (__str__) y que me permita identificar
#el país de origen , el numero de lote
def codprod():
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
            
    nameFile()   
    class Producto:
        def __init__(self, nombre, codigo):
            self.nombre = nombre
            self.codigo = codigo
        def __str__(self):
            lcod=self.codigo.split(sep="-")
            pais=lcod[0]
            lote=lcod[1]
            return '\nNombre: {} \nPaís: {} \nLote: {} '.format(self.nombre, pais,lote)

    #def infoprod():
    n=input('Nombre del producto: ').capitalize()
    c=input('Código de producto: ').upper()
    pr = Producto(n,c)
    print(pr)
#codprod()
#pr = Producto('Diamante','PERU-100-2023')
#print(pr)