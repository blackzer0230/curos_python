    ### SET ###
# Un set es una colección desordenada, mutable y sin elementos duplicados. 
# Se utilizan cuando la unicidad de los elementos y las operaciones de conjuntos (unión, intersección, etc.)
# son importantes.

# Dos formas de crear un set vacío
mi_set = set()               # Correcto: set vacío
mi_otro_set = {}              # ¡Cuidado! Esto crea un DICCIONARIO vacío, no un set

print(type(mi_set))           # <class 'set'>
print(type(mi_otro_set))      # <class 'dict'>  (por eso es importante no confundir)

# Para crear un set con elementos, usamos llaves pero con al menos un elemento
mi_otro_set = {"choso", "gonlez", 20}
print(type(mi_otro_set))      # Ahora sí es <class 'set'>
print(len(mi_otro_set))       # 3
print(mi_otro_set)

# agregar un elemento
mi_otro_set.add("sthefanny")
print(mi_otro_set) # el orden puede varias 

# Intentar agregar un elemento que ya existe
mi_otro_set.add("choso")
print(mi_otro_set) # no se agregar porque ya existe el elemento 

# Manera de comprobar que existe
print("choso" in mi_otro_set)   # True
print("chosi" in mi_otro_set)   # False

# ELIMINAR 
mi_otro_set.remove("gonlez") # lo elimina, si no existe da error
mi_otro_set.discard("TeAmo") # lo elimina, si no existe no dara error

elementos_eliminados = mi_otro_set.pop() # elimina elementos al azar
print(elementos_eliminados)

mi_otro_set.clear()
print(mi_otro_set)
print(len(mi_otro_set))


# convertir un set en una lista y viceversa
mi_set = {"choso", "gonlez", 20} #set
mi_lista = list(mi_set) # ahora es una lista

mi_set = set(mi_lista)

# operaciones de conjuntos 
set1 = {"harry", "gonlez", 20}
set2 = {"python", "go", "c++"}
union_set = set1.union(set2)
print(union_set)

    # tambien se pueden unir usando el operador |
otra_union_set = set1 | set2
print(otra_union_set)


# intersecciob de elementos comunes
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
interseccion = set_a.intersection(set_b)
print(interseccion)
    # o tambien
otra_interseccio = set_a & set_b
print(otra_interseccio)

# elmentos que estan en el primen set y no es el otro
diferencia = set_a.difference(set_b)
print(diferencia)

# diferencia que estan en uno u otro pero no en ambos 
sim_diff = set_a.symmetric_difference(set_b)
print(sim_diff)
































