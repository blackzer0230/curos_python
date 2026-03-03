    ### clases ### 
# las clases son como un molde que lo que puede hacer un objeto(instancias)
# para definir una clase usa la palabra reservada class

class MiClase: # los nombres de las clases tienen que ir en PascalCase
    pass # el pass significa que no haga nada para hacer una clase vacio

print(MiClase)
print(MiClase())

# crear una clase real
class persona:
    def __init__(self, name, surname, alias = "sin alias"): # el init es el condutor osea se ejecuta automaticamente
        self.name = name                                    # el self es un parametro obligatorio y se refiere el propio objeto que se esta creando
        self.__surname = surname # la propiedad se hace privada con el __
        self.fullname = f"{name} {surname} ({alias})"


    # para acceder a un metodo privado se crea una funcion que retorne el atributo
    def get_name(self):
        return self.__surname

    # metodos que pueden hacer un objeto
    def caminar(self):
        print(f"{self.fullname} esta caminando")

    #sigue crearle un objeto
harry = persona("harry", "gonzalez") # aqui harry es el objeto de la clase persona
print(harry.name) # tiene acceso 
print(harry.fullname) # se autocompleta con el valor predeterminado de alias
# print(harry.__surname) dara error porque es un atributo privado

# ahora para acceder al ese atriburo privado 
print(harry.get_name()) # ya se puede saber el apellido

# metodos que pueden hacer un objeto
harry.caminar()



# crear otro objeto mas claro
sthefanny = persona("sthefanny", "negodov", "tefy")
print(sthefanny.fullname)
print(sthefanny.get_name())
sthefanny.caminar()



# hay que tener cuidado porque se puede moficar cosas que no queramos
sthefanny.fullname = "ella es el amor de la vida de harry pero el la cago mucho"
print(sthefanny.fullname)