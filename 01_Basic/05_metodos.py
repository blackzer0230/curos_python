    ### metodos del sistema ###

lenguaje = "PorTugUes"

# CAMBIOS DE UN STRING 
print(lenguaje.capitalize()) # poner la primera ne mayuscula
print(lenguaje.upper()) # todas a mayusculas
print(lenguaje.lower())# todas a minusculas
print(lenguaje.swapcase()) # cambia las mayusculas por minusculas y viceversa
print(lenguaje.title()) # convierte todas las primeras letras de un palabra en mayuscula

# BUSCAR Y CONTAR
print(lenguaje.count("T")) # para buscar 
print(lenguaje.find("r")) # te dije el indice de lo que buscas
print(lenguaje.startswith("Por")) # empieza por cierto pre-fijo?
print(lenguaje.endswith("hola")) # termina por ciero su-fijo?

# VALIDAR CONTENIDO
print(lenguaje.isnumeric())
print("1".isnumeric()) # validar si es un numero
print("2".isalpha())
print(lenguaje.isalpha()) # validar si son letras
print(lenguaje.isalnum()) # validar si es un alfannumerico solo letras y numeros 
print(" ".isspace()) # solo es si es espcios solo 
print("HOLA".isupper()) # validar si es todo en mayuscula
print("hola".islower()) # validar si es todo en minuscula

# REEMPLAZAR Y SEPARAR
saludo = "hola,mundo"
print(saludo.replace("mundo", "python")) # remmplazar una palabra
print(saludo.split(",")) # separa por las comas

# LIMPIAR Y AJUSTAR ESPACIOS
my_salud = "  hola  "
perro = "kaneki"
print(my_salud.strip()) # elimina espacios o caracteres
print(perro.center(20, "-")) # centra en un campo asignado
print(perro.rjust(10, "-")) # rellena la izquierda 
print(perro.ljust(10, "-")) # rellena la derecha

