msg = """\nElija una de las siguientes operaciones:

a) Lista de categorías de libros.
b) Nombres de los libros y autores.
c) Cambiar estado de un libro a prestado.
d) Lista de usuarios de la biblioteca.

"""
biblioteca={
    'razón social':"Biblioteca Nacional",
    'categorias':["cuentos","novelas","ensayo","autobiografico","memorias","teatral","cientifico"],
    'usuarios':{
        "usuario1":{"nombre":"juan",
                    "apellido":"rodriguez",
                    "libro":[]
                    },
        "usuario2":{"nombre":"pedro",
                    "apellido":"ramos",
                    "libro":[]
                    }
    },
    'libro':{
        "BB234":{"titulo":"Pinocho",
                "autor":"Carlo Collodi",
                "estado":"prestado",
                "categoría":"cuentos"
                },
        "BB123":{"titulo":"IT",
                "autor":"Stephen King",
                "estado":"disponible",
                "categoría":"novelas"
                },
        "BB089":{"titulo":"Macbeth",
                "autor":"William Shakespeare",
                "estado":"disponible",
                "categoría":"teatral"
                }
    },
    "usuarioLibro":{
        "usuario1":[],
        "usuario2":[],
        "usuario3":[],
        "usuario4":[]
    } 
}
##inputs
print(msg)

opc=input('Ingresar la opción: ').upper()
print('Opción elegida: ',opc)

if(opc!='A' or opc!='B' or opc!='C'or opc!='D'):
    if opc=='A':
        print(biblioteca["categorias"])
    elif opc=='B':
        clib=input("Digite el codigo del libro: ")
        listaLibros=list(biblioteca["libro"].keys())
        if clib in listaLibros:
            print("\nLibro encontrado")
            titulo=biblioteca["libro"][clib]["titulo"]
            autor=biblioteca["libro"][clib]["autor"]
            #print(biblioteca["libro"])
            print(titulo)
            print(autor)
        else:
            print("Libro no encontrado")
    elif opc=='C':
        clib=input("Digite el codigo del libro: ")
        listaLibros=list(biblioteca["libro"].keys())
        if clib in listaLibros:
            print("\nLibro encontrado")
            biblioteca["libro"][clib]["estado"]="prestado"
            comprob=biblioteca["libro"][clib]["estado"]
            print("CAMBIADO A ",comprob)
        else:
            print("Libro no encontrado")
    elif opc=='D':
        #Crea lista
        lista = list()
        #Listar
        lista.append(biblioteca["usuarios"])
        print(lista)
    else:
        print('OPCION INVÁLIDA')
else:
    print('OPCIÓN INVALIDA')