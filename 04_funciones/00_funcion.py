    ### FOR ###
# Es un bloque de codigo que se puede reutilizar que hace una tarea especifica
# def nombre_de_la_funcion(parametros):
#    codigo de la funcion
#   return resultado # opcional el return

# funcion sin parametros 
def mi_funcion():
    print("esta es una funcion!!!")

mi_funcion()
mi_funcion()
mi_funcion() # llama a la funcion por su nombre reservado

# funcion con parametros
def suma(num1, num2): # son los parametros que recibira la funcion suma
    print(num1 + num2)

suma(5, 7)
suma(234, 3453456)
suma("6", "8") # en este caso se concatenan los strings

# funcion que devuelve un return
def segunda(num1, num2):
    mi_suma = num1 + num2
    return mi_suma

resultado = segunda(7, 8)
print(resultado)


# parametros con nombres
def nombres(name, surname):
    print(f"{name} {surname}")

nombres("gonzalez", "harry") # aqui tenemos un mini problema que se resuelve facil
nombres(surname="gonzalez", name="harry") # le asignamos en que parametro va cada valor


# parametros por defecto
def defecto(name, surmane, alias = "sin alias"):
    print(f"{name} {surmane} {alias}")

defecto("harry", "gonzalez") # el alias viene con uno por defecto pero se puede cambiar
defecto("harry", "gonzalez", "choso") # le cambiamos el valor por defecto


# numeros variables de argumentos
def argumentos(*texto):
    print(texto)
    print(type(texto))

argumentos("python", "go", "kotlin", "c++")


def argumentos(*texto):
    for text in texto:
        print(text)

argumentos("python", "go", "kotlin", "c++")