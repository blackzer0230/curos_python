         ### TUPLAS ###
# Una tupla es una estructura de datos similar a una lista, pero inmutable: una vez creada, 
# no se puede modificar (no se pueden añadir, eliminar ni cambiar elementos). Se usan para datos que no deben cambiar.

# Dos formas equivalentes:
mi_tupla = tuple()          # usando el constructor
mi_otra_tupla = ()           # usando paréntesis vacíos

# Tupla con elementos
mi_tupla = (20, 1.77, "choso", "gonlez")
print(mi_tupla)               # (20, 1.77, 'choso', 'gonlez')
print(type(mi_tupla))         # <class 'tuple'>


# Acceder a los elementos 
print(mi_tupla[0])    # 20
print(mi_tupla[2])    # "choso"
print(mi_tupla[-1])   # "gonlez"

# las tuplas solo tienen 2 metodos 

#  cuantas veces aparece un elemento
print(mi_tupla.count("gonlez"))   # 1

#  devuelve la posicion de la primera aparicin que aparezca
print(mi_tupla.index("choso"))    # 2


# las tuplas no se pueden modificar sus elementos 
# mi_tupla[0] = 30    ❌ Error: TypeError: 'tuple' object does not support item assignment


# si se necesita conviar un elemento de una lista solos se tiene que convertir en una lista y despues viseversa
# Convertir tupla a lista
mi_lista = list(mi_tupla)
print(type(mi_lista))          # <class 'list'>

# Modificar la lista
mi_lista[3] = "lovesthef"
mi_lista.insert(1, "negro")
print(mi_lista)                # [20, 'negro', 1.77, 'choso', 'lovesthef']

# Volver a tupla
mi_nueva_tupla = tuple(mi_lista)
print(mi_nueva_tupla)          # (20, 'negro', 1.77, 'choso', 'lovesthef')


























