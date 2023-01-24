##Pregunta 4

##Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
##clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
##tener un método para agregar productos y otra para mostrar toda la lista de productos

def tienda():
    def nameFile():
        if __name__=='__main__':
            print("\nAPP")
        else:
            print("\nSECUNDARIO")
            
    nameFile()   
    class Catalogo:
        productos = [] 
        
        def __init__(self,productos=[]):
            self.productos=productos

        def agregarp(self, pro):  # pro ->producto
            self.productos.append(pro)

        def mostrarp(self):
            print('\n<<<PRODUCTOS>>>')
            for pro in self.productos:
                print(pro)  

    class Producto:
        def __init__(self, precio, descripcion,stock):
            self.precio = precio
            self.descripcion = descripcion
            self.stock = stock
        def __str__(self):
            return '\nPrecio: {} \nDescripción: {} \nStock: {}'.format(self.precio, self.descripcion,self.stock)

    msg = "\nRegistrar Precio , Descripcion breve y Stock disponible:"


    print(msg)

    c = Catalogo()

    rpta='Si'
    #Añadir productos hasta respuesta negativa
    while rpta=='Si':
        pre=float(input('\nPrecio del producto: '))
        des=input('\nDescripcion: ')
        sto=int(input('\nStock disponible: '))
        pr = Producto(pre,des,sto)
    
        c.agregarp(pr)
        print('¿Desea agregar otro producto?')
        rpta=input('[Si/No]: ').capitalize()
    c.mostrarp()

#tienda()

