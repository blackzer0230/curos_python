        ### LISTAS ###
# Una lista es una estructura de datos que permite almacenar múltiples elementos en una sola variable. 
# Pueden ser de diferentes tipos (enteros, floats, strings, otras listas…) y son mutables, es decir, se pueden modificar después de creadas.

# Dos formas equivalentes:
mi_lista = list()        # usando el constructor
mi_otra_lista = []       # usando corchetes vacíos

# Lista con elementos
numeros = [10, 24, 17, 40, 40, 7, 65]
datos_persona = [20, 1.80, "Choso", "González"]

print(len(numeros))       # 7 → longitud de la lista
print(type(numeros))      # <class 'list'>


# Acceder a los elementos
print(datos_persona[0])    # 20
print(datos_persona[1])    # 1.8
print(datos_persona[-1])   # "González" (último)
print(datos_persona[-3])   # "Choso" (tercero empezando por el final)


# Contar apariciones de un elemento
print(datos_persona.count("Choso"))   # 1
print(numeros.count(40))              # 2


# Desempaquetar una lista
edad, altura, alias, apellido = datos_persona # debe coincidir el número de variables con la longitud de la lista 
print(apellido)   # "González"


# Concatenar listas
lista_concatenada = numeros + datos_persona
print(lista_concatenada)

# Mutabilidad y reasignación
mi_lista = [1, 2, 3]
mi_lista = "ahora soy un string"
print(mi_lista)          # "ahora soy un string"


######################


# Agrega un elemento al final.
datos_persona.append("love")
print(datos_persona)   # [20, 1.8, 'Choso', 'González', 'love']

# Inserta un elemento en una posición específica.
datos_persona.insert(1, "azul")
print(datos_persona)   # [20, 'azul', 1.8, 'Choso', 'González', 'love']

# Se puede cambiar directamente un elemento.
datos_persona[1] = "Rojo"
print(datos_persona)   # [20, 'Rojo', 1.8, 'Choso', 'González', 'love']

# Elimina la primera aparición del elemento indicado.
datos_persona.remove("Rojo")
print(datos_persona)   # [20, 1.8, 'Choso', 'González', 'love']

# Elimina y devuelve el elemento en la posición dada. Si no se pasa índice, elimina el último.
eliminado = datos_persona.pop()   # elimina 'love'
print(eliminado)                   # 'love'
print(datos_persona)               # [20, 1.8, 'Choso', 'González']

# Elimina un elemento por índice o incluso la variable completa.
del datos_persona[2]               # elimina 'Choso'
print(datos_persona)               # [20, 1.8, 'González']

# Vacía la lista por completo.
datos_persona.clear()
print(datos_persona)               # []

# Ordena la lista de forma ascendente (modifica la original)
numeros = [6, 5, 3, 2, 1]
numeros.sort()
print(numeros)           # [1, 2, 3, 5, 6]

# Invierte el orden de los elementos.
numeros.reverse()
print(numeros)           # [6, 5, 3, 2, 1]


# revanadas
mi_lista = [0, 1, 2, 3, 4, 5]
print(mi_lista[2:4])     # [2, 3]
print(mi_lista[:3])      # [0, 1, 2]  (desde el inicio hasta índice 2)
print(mi_lista[3:])      # [3, 4, 5]  (desde índice 3 hasta el final)
print(mi_lista[-3:])     # [3, 4, 5]  (los tres últimos)























